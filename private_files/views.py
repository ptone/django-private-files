import mimetypes
import os
import posixpath
import re
import urllib

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotModified
from django.core.exceptions import PermissionDenied
from django.db.models import get_model
from django.shortcuts import get_object_or_404
from django.contrib.admin.util import unquote
from django.views.static import was_modified_since
from django.utils.http import http_date, parse_http_date


def _handle_basic(request, instance, field_name):
    field_file  = getattr(instance, field_name)
    
    mimetype, encoding = mimetypes.guess_type(field_file.path)
    mimetype = mimetype or 'application/octet-stream'
    statobj = os.stat(field_file.path)
    if not was_modified_since(request.META.get('HTTP_IF_MODIFIED_SINCE'),
                              statobj.st_mtime, statobj.st_size):
        return HttpResponseNotModified(mimetype=mimetype)
    basename = os.path.basename(field_file.path)
    field_file.open()
    response = HttpResponse(field_file.file.read(), mimetype=mimetype)
    response["Last-Modified"] = http_date(statobj.st_mtime)
    response["Content-Length"] = statobj.st_size
    #response['Content-Disposition'] = 'attachment; filename=%s'%basename
    if encoding:
        response["Content-Encoding"] = encoding
    field_file.close()
    return response

    
def _handle_nginx(request, instance, field_name):
    response = HttpResponse(unicode(getattr(instance, field_name)))
    response["X-Accel-Redirect"] = unicode(getattr(instance, field_name))
    return response

def _handle_xsendfile(request, instance, field_name):
    field_file  = getattr(instance, field_name)
    basename = os.path.basename(field_file.path)
    mimetype, encoding = mimetypes.guess_type(field_file.path)
    mimetype = mimetype or 'application/octet-stream'
    statobj = os.stat(field_file.path)
    response = HttpResponse()
    response['Content-Type'] = mimetype
    response['Content-Disposition'] = 'attachment; filename="%s"' % basename
    response["X-Sendfile"] = field_file.path
    response['Content-Length'] = statobj.st_size
    return response

def get_file(request, app_label, model_name, field_name, object_id, filename):
    model = get_model(app_label, model_name)
    instance = get_object_or_404(model, pk =unquote(object_id))
    condition = getattr(instance, field_name).condition
    if not model:
        raise Http404("")
    if not hasattr(instance, field_name):
        raise Http404("")
    if condition(request, instance):
        return _handle_xsendfile(request, instance, field_name)
    else:
        raise PermissionDenied()
        