from flask_restx import Resource

def generic_controller(api, dto, service):
    model_input = dto['model_input']
    model = dto['model']
    model_filter = dto.get('model_filter')

    @api.route('/')
    class GenericAPI(Resource):

        @api.expect(model_input, validate=True)
        @api.marshal_with(model, code=201)
        def post(self):
            data = api.payload
            return service.create(data), 201

        @api.marshal_list_with(model)
        @api.expect(model_filter)            
        def get(self):
            query_params={}
            if model_filter:
                query_params = model_filter.parse_args()
            return service.get_all(query_params=query_params), 200
    return GenericAPI

def generic_id_controller(api, dto, service):
    model_input = dto['model_input']
    model = dto['model']


    @api.route('/<int:id>')
    @api.param('id','Identificador da entidade')
    class GenericIdAPI(Resource):

        @api.marshal_with(model)
        def get(self, id):
            return service.get(id), 200

        @api.expect(model_input, validate=True)
        @api.marshal_with(model)
        def put(self, id):
            data = api.payload
            return service.update(id, data), 200

        @api.response(204, 'Entidade deletada com sucesso')
        def delete(self, id):
        return bolsistaService.delete(id), 204

    return GenericIdAPI