# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:43:19 2021

@author: 191242
"""

import requests
import streamlit as st
    
def notify(msg, bearer, sticker=None, picURI=None, pic=None):
    headers = {
        "Authorization": "Bearer " + bearer 
							} 
    
    payload = {'message': msg}
    if sticker:
        payload["stickerPackageId"] = sticker[0]
        payload["stickerId"] = sticker[1]
    if picURI:
        payload["imageThumbnail"] = picURI
        payload["imageFullsize"] = picURI
    if pic:
        pic = {'imageFile': pic}
    
    r = requests.post("https://notify-api.line.me/api/notify",
                    headers = headers,
                    params = payload,
                    files=pic)
    return r.status_code


bearer = st.text_input('Bearer')
message = st.text_area('message')
if st.button('送出'):
    response = notify(message, bearer)
    st.write(response)
    
    
    
