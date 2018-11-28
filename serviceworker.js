var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilosmisperris.css', //estilos
    '/static/core/img/logo.png',  //logo mis perris
    '/static/core/img/perro.png', //imagen perro
    '/static/core/img/Adoptados/Apolo.jpg',  //apolo
    '/static/core/img/Adoptados/Duque.jpg',  //duque
    '/static/core/img/Adoptados/Tom.jpg',    //tom
    '/static/core/img/socialfacebook.png',  //face
    '/static/core/img/socialplus.png',      //google
    '/static/core/img/social-inst.png',     //insta
    '/static/core/img/Correo.png',          //correo
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',  //1
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js', //2
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.css', //3
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.3.5/jquery.fancybox.min.js', //4
    '/static/core/js/inicializacionmisperris.js',  //inicializacion
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
           

            return fetch(event.request).catch(function(){
                return response
            })
        })
    );
});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

  // Initialize Firebase
  // Initialize Firebase
var config = {
    apiKey: "AIzaSyAM-gOFYP6xW2j22npwNdthQgKtctLnH3k",
    authDomain: "mis-perris-237d2.firebaseapp.com",
    databaseURL: "https://mis-perris-237d2.firebaseio.com",
    projectId: "mis-perris-237d2",
    storageBucket: "mis-perris-237d2.appspot.com",
    messagingSenderId: "347078296310"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

//programamos una funcion que estara escuchando cuando llegue una
//notificacion desde firebase

messaging.setBackgroundMessageHandler(function(payload) {

    //el payload contendrá el mensaje destinado al usuario
    var title = "notificacion"
    var options = {
        body:"este es el cuerpo del mensaje"
    }

    //mostramos la notificacion al usuario
    return self.registration.showNotification(title, options);

})
