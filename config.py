#!/usr/bin/env python3
# encoding: utf-8

import os


class Config(object):

    #############node节点#####################
    BOOTSTRAP_NODES = (
        ('router.bittorrent.com', 6881),
        ('dht.transmissionbt.com', 6881),
        ('router.utorrent.com', 6881)
    )

    ###############爬虫配置###################
    # 掉线后重新加入DHT网络的时间间隔
    REJOIN_DHT_INTERVAL = 3
    # 绑定IP
    BIND_IP = '0.0.0.0'
    # 绑定端口    
    BIND_PORT = 11158
    # 最大节点数
    MAX_NODE_SIZE = int(os.environ.get('MAX_NODE_SIZE', '1000'))
    # 最大下载数
    DOWNLOAD_THREAD = int(os.environ.get('DOWNLOAD_THREAD', '1000'))

    ################mongo配置#################
    # MONGO_HOST = os.environ.get('MONGO_HOST', '140.143.208.158')
    # MONGO_PORT = int(os.environ.get('MONGO_PORT', '27017'))

    ################redis配置##################
    # redis key
    REDIS_KEY = "infohash"
    # redis 地址
    REDIS_HOST = "39.108.218.149"
    # redis 端口
    REDIS_PORT = 6379
    # redis 密码
    REDIS_PASSWORD = None
    # redis 连接池最大连接量
    REDIS_MAX_CONNECTION = 20

    ################elasticsearch配置##################
    # elastics 地址
    ELASTICS_HOST = "39.108.218.149"
    # elastics 端口
    ELASTICS_PORT = 9200
    # elastics 密码
    ELASTICS_PASSWORD = None
    # elastics 连接池最大连接量
    ELASTICS_MAX_CONNECTION = 20
