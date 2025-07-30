#!/usr/bin/env python
import os
import django

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loja_carros.settings')
django.setup()

from vendas.models import Carro

def populate_cars():
    cars_data = [
        {
            'marca': 'ford',
            'modelo': 'Fiesta',
            'ano': 2020,
            'preco': 45000.00,
            'quilometragem': 25000,
            'combustivel': 'flex',
            'cor': 'Branco',
            'descricao': 'Ford Fiesta 2020 em excelente estado, único dono, revisões em dia. Carro econômico e ideal para cidade.',
            'disponivel': True
        },
        {
            'marca': 'chevrolet',
            'modelo': 'Onix',
            'ano': 2021,
            'preco': 55000.00,
            'quilometragem': 18000,
            'combustivel': 'flex',
            'cor': 'Prata',
            'descricao': 'Chevrolet Onix 2021, seminovo, muito bem conservado. Excelente para família.',
            'disponivel': True
        },
        {
            'marca': 'volkswagen',
            'modelo': 'Golf',
            'ano': 2019,
            'preco': 75000.00,
            'quilometragem': 35000,
            'combustivel': 'gasolina',
            'cor': 'Preto',
            'descricao': 'Volkswagen Golf 2019, carro esportivo e elegante. Performance excepcional.',
            'disponivel': True
        },
        {
            'marca': 'honda',
            'modelo': 'Civic',
            'ano': 2020,
            'preco': 85000.00,
            'quilometragem': 22000,
            'combustivel': 'flex',
            'cor': 'Azul',
            'descricao': 'Honda Civic 2020, sedan esportivo, confortável e seguro. Ideal para viagens.',
            'disponivel': True
        },
        {
            'marca': 'toyota',
            'modelo': 'Corolla',
            'ano': 2021,
            'preco': 90000.00,
            'quilometragem': 15000,
            'combustivel': 'flex',
            'cor': 'Branco',
            'descricao': 'Toyota Corolla 2021, seminovo, muito bem conservado. Carro confiável e econômico.',
            'disponivel': True
        },
        {
            'marca': 'bmw',
            'modelo': '320i',
            'ano': 2018,
            'preco': 120000.00,
            'quilometragem': 45000,
            'combustivel': 'gasolina',
            'cor': 'Cinza',
            'descricao': 'BMW 320i 2018, carro de luxo em excelente estado. Performance e conforto.',
            'disponivel': True
        }
    ]
    
    for car_data in cars_data:
        car, created = Carro.objects.get_or_create(
            modelo=car_data['modelo'],
            ano=car_data['ano'],
            defaults=car_data
        )
        if created:
            print(f"Carro criado: {car}")
        else:
            print(f"Carro já existe: {car}")

if __name__ == '__main__':
    print("Populando banco de dados com carros de exemplo...")
    populate_cars()
    print("Concluído!") 