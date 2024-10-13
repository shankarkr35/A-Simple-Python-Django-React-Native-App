import datetime
import os
import random
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import *
from .serializers import *
from rest_framework import status
from apps.employees.models import Employee
from django.contrib.auth import get_user_model
User = get_user_model() 
import jwt 
from datetime import timedelta
from rest_framework.exceptions import AuthenticationFailed
from jwt import decode, ExpiredSignatureError 
from middlewares.driverVerifyToken import driver_token_required
from django.contrib.auth.hashers import check_password
from django.utils import timezone  # Use Django's timezone utility
from apps.sectors.models import Sector