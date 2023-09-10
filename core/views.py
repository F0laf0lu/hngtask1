from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
import pytz

# Create your views here.
def get_user_info(request):
    slack_name = request.GET.get('slack_name', 'Folafolu Osilaja')
    track = request.GET.get('track', 'Backend')

    current_day = timezone.now().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_repo_url = "https://github.com/F0laf0lu/hngtask1"
    github_file_url = "https://github.com/F0laf0lu/hngtask1/blob/main/core/views.py"


    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return JsonResponse(response_data)

