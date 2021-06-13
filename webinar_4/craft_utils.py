def prefilter_items(data, item_features, take_n_popular=5000):

    filtered_items = []
    # Уберем самые популярные товары (их и так купят)
    popularity = data.groupby('item_id')['user_id'].nunique().reset_index() / data['user_id'].nunique()
    popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)

    # Уберем самые популярные товары (их и так купят)
    filtered_items.append(popularity[popularity['share_unique_users'] > 0.5].item_id.tolist())

    # Уберем самые НЕ популярные товары (их и так НЕ купят)
    filtered_items.append(popularity[popularity['share_unique_users'] < 0.01].item_id.tolist())

    # Уберем товары, которые не продавались за последние 12 месяцев

    # Уберем не интересные для рекоммендаций категории (department)

    # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.

    # Уберем слишком дорогие товарыs

    # ...
    # Уберем из датасета отфильтрованные выше items, чтобы найти топ заданных среди оставшихся
    data_sorted = data[~data['item_id'].isin(filtered_items)]

    popularity_n = data_sorted.groupby('item_id')['quantity'].sum().reset_index()
    popularity_n.rename(columns={'quantity': 'n_sold'}, inplace=True)
    top_5000 = popularity_n.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()

    # Поставим флаги для фильтрации
    data.loc[~data['item_id'].isin(top_5000), 'item_id'] = 999999

    return data


def postfilter_items(user_id, recommednations):
    pass


def postfilter_items(user_id, recommednations):
    pass