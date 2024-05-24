from django.urls import path

from . import views


urlpatterns = [
    path("chats/", views.chat_list, name="chats-list"),
    path("api/v1/chats/", views.ChatRoomListAPI.as_view(), name="api-chats-list"),
    path("chat/<str:chat_room_id>/", views.chat_room, name="chat-room"),
    path(
        "api/v1/chat/<str:chat_room_id>/",
        views.ChatRoomAPI.as_view(),
        name="api-chat-room",
    ),
    # API endpoint to update read receipt of message
    path(
        "api/messages/v1/<int:message_id>/update/",
        views.update_message,
        name="update_message",
    ),
    path(
        "api-token-auth/", views.ObtainTokenPairView.as_view(), name="token_obtain_pair"
    ),
]
