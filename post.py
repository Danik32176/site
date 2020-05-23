import datetime

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

class Post:

    @staticmethod
    async def create_post(db:AsyncIOMotorDatabase, user_id: str, message: str):
        data = {
            'user_id': ObjectId(user_id),
            'message': message,
            'data_created': datetime.utcnow()
        }
        await db.posts.insert_one(data)

    @staticmethod
    async def get_posts_by_user(db:AsyncIOMotorDatabase, user_id: str, limit= 20):
        posts = await db.posts.find({'user_id': ObjectId(user_id)}).to_lists(limit)
        return posts