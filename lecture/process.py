# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)

     if not pdf.err:
          # response = HttpResponse(content_type='application/pdf')
          # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
          return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response