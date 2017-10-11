<template>
    <div>
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{ t('faq_title') }}</h1>
            </div>
        </div>
        <bread-crumbs :crumbs="crumbs"></bread-crumbs>

        <div class="space-60"></div>

        <div class="container">
            <div class="row">
                <div class="col-md-6 about-img">
                    <img src="../../img/faq-bg.jpg" />
                </div>
                <div class="col-md-6">
                    <br>
                    <h3>Question 1</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
                        maxime placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque
                        nihil impedit quo minus id quod maxime placeat facere possimus.</p>
                    <h3>Question 2</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
                        maxime placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque
                        nihil impedit quo minus id quod maxime placeat facere possimus.</p>
                    <h3>Question 3</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
                        maxime placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque
                        nihil impedit quo minus id quod maxime placeat facere possimus.</p>
                    <h3>Question 4</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
                        maxime placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque
                        nihil impedit quo minus id quod maxime placeat facere possimus.</p>
                    <h3>Question 5</h3>
                    <p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
                        maxime placeat facere possimusNam libero tempore, cum soluta nobis est eligendi optio cumque
                        nihil impedit quo minus id quod maxime placeat facere possimus.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import BreadCrumbs from '../main/Breadcrumbs.vue'

    export default {
         locales: {
            es_ES: {
                faq_title: 'Preguntas frecuentes',
            },
            en_US: {
                faq_title: 'Frequently asked questions',
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
                         es: 'Preguntas frecuentes',
                         en: 'Frequently asked questions'
                     }
                 }
            }
        },
        components: {
            BreadCrumbs
        }
    }
</script>