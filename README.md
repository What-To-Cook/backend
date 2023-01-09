# backend
Backend for "What To Cook?" application, which allows retrieving available ingredients and select recipes based on your 
kitchen content, your allergies and preferences.

## Usage
Clone the repository:
```
git clone https://github.com/What-To-Cook/backend.git
cd backend
```

Create **.env** file in the root directory with the following contents:
```
MONGO_HOST=localhost
# based on docker-compose.dev.yml file
MONGO_PORT=27017
MONGO_USER=root
MONGO_PASSWORD=example
```

Build Docker image:
```
docker compose -f docker-compose.dev.yml build
```

Start Mongo, Mongo Express and backend services:
```
docker compose -f docker-compose.dev.yml up -d
```

Add some recipes to the database. You can use [this parser](https://github.com/What-To-Cook/recipe-parser) for it, or 
you can just do it yourself (but please, follow [the structure](https://github.com/What-To-Cook/recipe-parser#recipes-structure) 
for every recipe).

After successful startup, you can find services listening on the following ports:
- 27017 for Mongo
- 8081 for Mongo Express
- 12000 for API

## API endpoints
### Endpoint /ingredients
Allows retrieving available ingredients.
#### Example request
```
curl --location --request GET 'http://0.0.0.0:12000/ingredients'
```

#### Example response
```["Бекон", "Ванилин", "Ванильный экстракт", "Гашеная сода"]```

### Endpoint /recipes
Allows selecting recipes based on available ingredients, allergies and preferences.
#### Example request
```
curl --location --request GET 'http://0.0.0.0:12000/recipes' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ingredients": [
        "Темный шоколад",
        "Коричневый сахар",
        "Пшеничная мука",
        "Грецкие орехи",
        "Сливочное масло",
        "Куриное яйцо",
        "a"
    ],
    "allergies": [
        "Яблоко"
    ]
}'
```

#### Example response
```
[
    {
        "name": "Брауни (brownie)",
        "serves_amount": 6,
        "steps": [
            "Шоколад разломать на кусочки и вместе со сливочным маслом растопить на водяной бане, не переставая все время помешивать лопаткой или деревянной ложкой. Получившийся густой шоколадный соус снять с водяной бани и оставить остывать.",
            "Тем временем смешать яйца со ста граммами коричневого сахара: яйца разбить в отдельную миску и взбить, постепенно добавляя сахар. Взбивать можно при помощи миксера или вручную — как больше нравится, — но не меньше двух с половиной-трех минут.",
            "Острым ножом на разделочной доске порубить грецкие орехи. Предварительно их можно поджарить на сухой сковороде до появления аромата, но это необязательная опция.",
            "В остывший растопленный со сливочным маслом шоколад аккуратно добавить оставшийся сахар, затем муку и измельченные орехи и все хорошо перемешать венчиком.",
            "Затем влить сахарно-яичную смесь и тщательно смешать с шоколадной массой. Цвет у теста должен получиться равномерным, без разводов.",
            "Разогреть духовку до 200 градусов. Дно небольшой глубокой огнеупорной формы выстелить листом бумаги для выпечки или калькой. Перелить тесто в форму. Поставить в духовку и выпекать двадцать пять — тридцать минут до появления сахарной корочки.",
            "Готовый пирог вытащить из духовки, дать остыть и нарезать на квадратики острым ножом или ножом для пиццы — так кусочки получатся особенно ровными.",
            "Подавать брауни можно просто так, а можно посыпать сверху сахарной пудрой или разложить квадратики по тарелкам и украсить каждую порцию шариком ванильного мороженого."
        ],
        "ingredients": [
            {
                "ingredient": "Темный шоколад",
                "amount": "100 г"
            },
            {
                "ingredient": "Сливочное масло",
                "amount": "180 г"
            },
            {
                "ingredient": "Коричневый сахар",
                "amount": "200 г"
            },
            {
                "ingredient": "Куриное яйцо",
                "amount": "4 штуки"
            },
            {
                "ingredient": "Пшеничная мука",
                "amount": "100 г"
            },
            {
                "ingredient": "Грецкие орехи",
                "amount": "100 г"
            }
        ],
        "energy_value_per_serving": {
            "calories": 676,
            "protein": 10,
            "fat": 46,
            "carbohydrates": 55
        }
    }
]
```