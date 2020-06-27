import base64
import io

from django.views.generic import CreateView
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import File
from .serializer import get_files


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        data = reversed(get_files())
        return render(request, "home.html", {"files": data})


class UploadFileView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, "add_file.html")

    def post(self, request, *args, **kwargs):
        if request.POST.get("path"):
            header, data = request.POST["path"].split(";base64,")
            if "pdf" not in header:
                return JsonResponse(
                    data={
                        "text": "File not pdf! Please upload a pdf.",
                        "level": "danger",
                    },
                    status=403,
                )

            pdf_file = io.BytesIO(base64.b64decode(data))
            django_file = InMemoryUploadedFile(
                pdf_file,
                field_name="path",
                name=request.POST.get("name"),
                content_type="application/json",
                size=request.POST.get("size"),
                charset=None,
            )
            File.objects.create(
                name=request.POST.get("name"),
                size=request.POST.get("size"),
                path=django_file,
            )
            return JsonResponse(
                data={"text": "File uploaded!", "level": "success"}, status=201
            )

        return JsonResponse(
            data={
                "text": "Could not upload file. Please try again!",
                "level": "danger",
            },
            status=403,
        )
