from .utils import *

class EmployeeLoginView(APIView):
    def post(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            emp = Employee.objects.filter(email=email).first()
            if emp is not None:
                if check_password(password, emp.password):
                    expiry = timezone.now() + timedelta(minutes=60)
                    issued_time = int(timezone.now().timestamp())

                    # JWT payload
                    payload = {
                        'emp_id': emp.id,
                        'expiry': expiry.strftime('%Y-%m-%d %H:%M:%S'),
                        'iat': issued_time,
                    }

                    # Encode the payload as a JWT
                    jwt_token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')

                    if emp.status == True:
                        response = Response()
                        response.set_cookie(key='emp_token',value=jwt_token,httponly=True)
                        response.data = {
                            'success': True,
                            'msg': 'Login Success!',
                            'status': status.HTTP_200_OK,
                            'token': jwt_token,
                            'responseData': {
                                'emp_id': emp.id,
                                'name': emp.name,
                                'mobile_number': str(emp.mobile_number),
                                'email': emp.email,
                            }
                        }
                        return response
                    else:
                        response_data = {
                            'success': False,
                            'msg': 'Login Failed',
                            'errors': "Account is not active please contact to admin!",
                            'status': status.HTTP_400_BAD_REQUEST,
                        }
                        return Response(response_data, status=status.HTTP_400_BAD_REQUEST) 
                else:
                    return Response({
                        'success': False,
                        'msg': 'Login Failed',
                        'errors': "Incorrect Password!",
                        'status': status.HTTP_400_BAD_REQUEST,
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                response_data = {
                    'success': False,
                    'msg': 'Login Failed',
                    'errors': "Incorrect Email Address!",
                    'status': status.HTTP_400_BAD_REQUEST,
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            response_data = {
                'success': False,
                'msg': f'Login Failed: {str(e)}',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Sectors(APIView):
    def get(self,request):
        try:
            sectors = Sector.objects.filter(status=True)
            serializer = SectorSerializer(sectors, many=True)
            response_data = {
                'success': True,
                'msg': "data found!",
                'status': status.HTTP_200_OK,
                'data':serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {
                'success': False,
                'msg': f'Login Failed: {str(e)}',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)