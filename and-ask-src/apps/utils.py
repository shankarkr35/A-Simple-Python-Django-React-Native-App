from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from middlewares.auth import auth_middleware,auth_company_middleware
from apps.employees.models import Employee
from django.db.models import Q
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from apps.sectors.models import Sector
import json

import pandas as pd
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()