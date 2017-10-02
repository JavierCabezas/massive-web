<template>
    <div>
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{ t('about_us') }} </h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>

        <div class="space-60"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h3>Videogames Music for All!</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime
                        placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit
                        quo minus id quod maxime placeat facere possimus.</p>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime
                        placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit
                        quo minus id quod maxime placeat facere possimus.</p>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime
                        placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit
                        quo minus id quod maxime placeat facere possimus.</p>
                    <br>
                </div>
                <div class="col-md-6 about-img">
                    <img src="../../img/about-bg.jpg"/>
                </div>
            </div>
        </div>
        <div class="space-60"></div>
    </div>
</template>

<script>
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
         locales: {
            es_ES: {
                about_us: 'Sobre nosotros',
            },
            en_US: {
                about_us: 'About us',
            }
        },
        data () {
            return {
                 crumbs: {
                     nav: [
                         {
                             link: 'home',
                             name_en: 'Home',
                             name_es: 'Inicio'
                         }
                     ],
                     current: {
                         es: 'Sobre nosotros',
                         en: 'About us'
                     }
                 }
            }
        },
        components: {
            BreadCrumbs
        }
    }
</script>