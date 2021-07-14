from flask_restful import Resource
from models.item import ItemModel
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}

    def put(self, name):
        store = StoreModel.find_by_name(name)

        if store is None:
            store = StoreModel(name)
        store.save_to_db()

        return store.json()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
