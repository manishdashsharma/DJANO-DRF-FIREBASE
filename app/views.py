from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from config.dbconfig import *
import json
from .serializers import *

@method_decorator(csrf_exempt, name='dispatch')
class serviceInfo(APIView):
    def get(self, request ):
        return Response({
            "success": True,
            "message":"Welcome to our API service."
        },status=status.HTTP_200_OK)
    
@method_decorator(csrf_exempt, name='dispatch')
class user_info(APIView):
    def post(self, request):
        name = request.data.get('name')
        location = request.data.get('location')

        serializer = CreateUserSerializer(data={
            "name": name,
            "location": location
        })

        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": "Invalid data provided",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        response = database.push({
            "name": name,
            "location": location
        })

        return Response({
            "success": True,
            "message": "User created successfully",
            "response": {
                "_id": response["name"],
                "name": name,
                "location": location
            }
        }, status=status.HTTP_201_CREATED)
        
        
    def get(self, request):
        user_details_response = database.get().val()

        user_responses = []

        for user_id, user_details in user_details_response.items():
            response = {
                "_id": user_id,
                "name": user_details.get("name", ""),
                "location": user_details.get("location", "")
            }
            user_responses.append(response)

        return Response({
            "success": True,
            "message": "Retrieved all users information",
            "response": user_responses
        }, status=status.HTTP_200_OK)
    
    def put(self, request):
        user_id = request.data.get("user_id")
        update_data = request.data.get("update_data")

        serializer = UpdateUserSerializer(data={
            "user_id": user_id,
            "update_data": update_data
        })

        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": "Invalid data provided",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        response = database.child(user_id).update(update_data)
        
        return Response({
            "success": True,
            "message": "User updated successfully",
            "response":response
        }, status=status.HTTP_200_OK)
    
    def delete(self, request):
        user_id = request.data.get("user_id")

        response = database.child(user_id).remove()

        return Response({
            "success": True,
            "message": "User deleted successfully"
        }, status=status.HTTP_200_OK)
