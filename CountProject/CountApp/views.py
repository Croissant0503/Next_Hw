from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)

    without_blank_len = 0
    word_cnt = 1


    for char in text:
        if char != ' ':
            without_blank_len += 1
        else:
            word_cnt += 1

    return render(request, 'result.html', {
        'text': text,
        'total_len': total_len,
        'without_blank_len': without_blank_len,
        'word_cnt': word_cnt,
        })