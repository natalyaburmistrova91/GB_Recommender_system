def prefilter_items(data, item_features, take_n_popular=5000):
    # Уберем самые популярные товары (их и так купят)
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    top_popular = popularity[popularity['share_unique_users'] > 0.5].item_id.tolist()
    data_result = data[~data['item_id'].isin(top_popular)]

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    top_notpopular = popularity[popularity['share_unique_users'] < 0.01].item_id.tolist()
    data_result = data_result[~data_result['item_id'].isin(top_notpopular)]

    # Уберем товары, которые не продавались за последние 12 месяцев

    # Уберем не интересные для рекоммендаций категории (department)

    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.

    # Уберем слишком дорогие товарыs

    # ...
    # Обработка data

    # Уберем из датасета отфильтрованные выше items, чтобы найти топ заданных среди оставшихся
    items_sorted = data_result.groupby('item_id')['item_id'].nunique().tolist()
    data_sorted = data.loc[~data['item_id'].isin(items_sorted)]

    popularity_n = data_sorted.groupby('item_id')['quantity'].sum().reset_index()
    popularity_n.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_5000 = popularity_n.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()

    # Поставим флаги для фильтрации
    data.loc[~data['item_id'].isin(items_sorted), 'item_id'] = 999999
    data.loc[~data['item_id'].isin(top_5000), 'item_id'] = 999999

    return data


def postfilter_items(user_id, recommednations):
    pass


def postfilter_items(user_id, recommednations):
    pass