
from django.shortcuts import render
import pandas as pd
def index(request):
    context={}
    if request.method=="POST":
        df=pd.read_excel(request.FILES["file"])
        context = {
                'columns': df.columns.tolist(),
                'total_rows': len(df),
                'sample_data': df.to_html(),
            }
    return render(request,"index.html",context=context)
