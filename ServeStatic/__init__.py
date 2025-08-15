import os, mimetypes
import azure.functions as func

def _safe_join(base_dir, *paths):
    final_path = os.path.normpath(os.path.join(base_dir, *paths))
    if not final_path.startswith(os.path.normpath(base_dir)):
        raise ValueError("Invalid path")
    return final_path

def main(req: func.HttpRequest) -> func.HttpResponse:
    public_dir = _safe_join(os.path.dirname(__file__), '..', 'public')
    request_path = (req.route_params.get('path') or '').lstrip('/')
    target = _safe_join(public_dir, request_path)
    if not request_path or os.path.isdir(target) or not os.path.exists(target):
        target = _safe_join(public_dir, 'index.html')
    with open(target, 'rb') as f:
        data = f.read()
    mime = mimetypes.guess_type(target)[0] or 'application/octet-stream'
    headers = {'Content-Type': f"{mime}; charset=utf-8"} if mime.startswith('text/') else {'Content-Type': mime}
    if not target.endswith('.html'):
        headers['Cache-Control'] = 'public, max-age=3600'
    return func.HttpResponse(body=data, status_code=200, headers=headers)
