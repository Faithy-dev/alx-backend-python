#!/usr/bin/env python3
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Extend the default Django User here with additional fields if needed
    # For now, just an example: add a 'bio' field
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Conversation(models.Model):
    # Many-to-many relationship between users and conversations
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        participant_usernames = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation between {participant_usernames}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"
