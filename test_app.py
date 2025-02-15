import pytest
import pandas as pd
from app.preprocessor import create_dataframe, create_dataframe_json
import json
import io

def test_whatsapp_dataframe():
    sample = [
            "04/01/22, 10:09 pm - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more."
            "04/01/22, 10:09 pm - ~ mohan created group college group❤️"
            "04/01/22, 10:09 pm - ~ mohan added you"
            "04/01/22, 10:09 pm - +91 11111 22222: Hii guys"
            "04/01/22, 10:09 pm - +91 22222 33333: Many asked me for official group so I have created"
            "04/01/22, 10:09 pm - prakash: Ohh"
            "04/01/22, 10:09 pm - ~ mohan cool"
            " 04/01/22, 10:09 pm - +91 22222 44444: U can help eachother and make use of it"
            "04/01/22, 10:10 pm - +91 22222 55555: 😂✌️"
            ]
    result = create_dataframe(sample)
    assert isinstance(result, pd.DataFrame)

def test_telegram_dataframe():
    sample = {
    "name": "EduConnect Community",
    "type": "public_channel",
    "id": 1234567890,
    "messages": [
        {
            "id": 1,
            "type": "service",
            "date": "2023-09-01T08:00:00",
            "date_unixtime": "1693555200",
            "actor": "EduConnect Community",
            "actor_id": "channel1234567890",
            "action": "create_channel",
            "title": "STEM Learning Resources",
            "text": "",
            "text_entities": []
        },
        {
            "id": 1023,
            "type": "message",
            "date": "2024-02-01T10:30:00",
            "date_unixtime": "1706783400",
            "edited": "2024-02-05T12:00:00",
            "edited_unixtime": "1707134400",
            "from": "EduConnect Community",
            "from_id": "channel1234567890",
            "photo": "(File not included. Change data exporting settings to download.)",
            "width": 1280,
            "height": 720,
            "text": [
                "🎓 **Welcome to EduConnect Community!** 🎓\n\nWe are thrilled to provide a space for students, educators, and lifelong learners to access **quality educational resources** in STEM, humanities, and more! Our mission is to foster knowledge-sharing, discussions, and collaboration for academic success. 🚀\n\n📌 ",
                {
                    "type": "text_link",
                    "text": "Explore Learning Hub",
                    "href": "https://t.me/EduConnect_Hub"
                }
            ],
            "text_entities": [
                {
                    "type": "plain",
                    "text": "🎓 **Welcome to EduConnect Community!** 🎓\n\nWe are thrilled to provide a space for students, educators, and lifelong learners..."
                },
                {
                    "type": "text_link",
                    "text": "Explore Learning Hub",
                    "href": "https://t.me/EduConnect_Hub"
                }
                ]
            }
        ]
    }

    sample_json = json.dumps(sample, indent=4)
    file_like_object = io.StringIO(sample_json)
    _,result = create_dataframe_json(file_like_object)
    assert isinstance(result, pd.DataFrame)