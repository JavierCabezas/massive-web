<template>
    <nav class="navbar navbar-default navbar-static-top yamm">
        <div class="container">
            <div class="navbar-header col-sm-12 col-md-6 col-lg-4">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-controls="navbar">
                    <span class="sr-only">MassiveWave</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#"><img src="../../img/mw-logo2.png" alt="logo"></a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><router-link :to="{name: 'home'}"> {{ t('home') }} </router-link></li>
                    <li><router-link :to="{name: 'about-us'}">{{ t('about') }}</router-link></li>
                    <li><router-link :to="{name: 'music-packs'}"> {{ t('music_pack') }} </router-link></li>
                    <li><router-link :to="{name: 'music-tracks'}"> {{ t('music_track') }} </router-link></li>
                    <li><router-link :to="{name: 'faq'}">{{ t('faq') }}</router-link></li>
                    <li><router-link :to="{name: 'blog'}">Blog</router-link></li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        locales: {
            es_ES: {
                home: 'Inicio',
                about: 'Sobre nosotros',
                music_pack: 'Packs de música',
                music_track: 'Canciones sueltas',
                faq: 'Preguntas frecuentes',
            },
            en_US: {
                home: 'Home',
                about: 'About us',
                music_pack: 'Music packs',
                music_track: 'Music tracks',
                faq: 'FAQ',
            }
        },
        mounted: function() {
            $( window ).resize(function() {
                $(".navbar-collapse").css({ maxHeight: $(window).height() - $(".navbar-header").height() + "px" });
            });

        }
    }
</script>