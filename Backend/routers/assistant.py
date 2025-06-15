from fastapi import APIRouter
from models.interaction import UserInteraction
from db.database import db
from services.youtube import search_youtube

router = APIRouter()

@router.post("/interact")
async def handle_interaction(interaction: UserInteraction):
    try:
        # Your logic here
        response_message = "I'm not sure how to respond yet."
        if "play" in interaction.user_input.lower() and "youtube" in interaction.user_input.lower():
            media_url = await search_youtube(interaction.user_input)
            response_message = "Playing video now."
            # Don't return media_url if it's problematic

        # Store in DB - comment this out temporarily to test
        # await db.interactions.insert_one(interaction.dict())

        return {"message": response_message}

    except Exception as e:
        return {"error": str(e)}
