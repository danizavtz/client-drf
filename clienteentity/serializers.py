from rest_framework import serializers
from clienteentity.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Cliente
		fields =  ('id', 'login', 'email', 'phone',)

	# def create(self, validated_data):
	# 	"""
	# 	Cria e retorna um novo cliente
	# 	"""
	# 	return Cliente.objects.create(**validated_data)

	# def update(self, instance, validated_data):
	# 	"""
	# 	Atualiza e retorna um Cliente
	# 	"""
	# 	instance.login = validated_data.get('login', instance.login)
	# 	instance.email = validated_data.get('email', instance.email)
	# 	instance.phone = validated_data.get('phone', instance.phone)
	# 	instance.save();
	# 	return instance;