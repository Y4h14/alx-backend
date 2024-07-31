#!/usr/bin/node
const express = require('express');
const {createClient} = require('redis');
const {promisify} = require('util');

const app = express();
const client = createClient();

const listProducts = [
{'itemId': 1, 'itemName': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4},
{'itemId': 2, 'itemName': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10},
{'itemId': 3, 'itemName': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2},
{'itemId': 4, 'itemName': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5}
]

const getItemById = (id) => {
    const item = listProducts.find(obj => obj.itemId == id);
    if(item) {
        return item;
    }
}

const reverseStockById = (itemId, stock) => {
    const item = getItemById(itemId);
    client.SET(item.itemId, stock);
}

const getCurrentReservedStockById = (itemId) => {
    return promisify(client.get).bind(client)(`item.${itemId}`);
}

app.get('/list_products', (_,res) => {
    res.send(listProducts);
});

app.get('/list_products/:itemId(\\d+)', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    
    if (item) {
        getCurrentReservedStockById(itemId)
        .then((result) => Number.parseInt(result || 0))
        .then((reservedStock) => {
            item.currentQuantity = item.initialAvailableQuantity - reservedStock;
            res.send(item);
        });

    } else {
        res.send({'status': 'Product not found'});
    }

});

app.get('/reserve_product/:itemId(\\+d)', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);

    if (!item) {
        res.send({'status': 'Product not found'});
    }

    getCurrentReservedStockById(itemId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
        if (reservedStock >= item.initialAvailableQuantity) {
            res.send({'status':'Not enough stock available','itemId':1});
        } else {

            reserveStockById(itemId, reservedStock + 1);
            res.send({'status':'Reservation confirmed','itemId':itemId});
        }
    });
});

app.listen(1245, () => {
    console.log('listining on port 1245');
});

