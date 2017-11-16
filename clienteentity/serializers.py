from rest_framework import serializers
from clienteentity.models import Cliente

class ClienteentitySerializer(serializers.ModelSerializer):
	class Meta:
		model  = Cliente
		fields =  ('id', 'login', 'email', 'phone')

	def create(self, validated_data):
		"""
		Cria e retorna um novo cliente
		"""
		return Clienteentity.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Atualiza e retorna um Cliente
		"""
		instance.login = validated_data.login
		instance.email = validated_date.email
		instance.phone = validated_date.phone
		instance.save();
		return instance;