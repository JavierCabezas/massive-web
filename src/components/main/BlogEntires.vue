<template>
    <section class="new-arrivals new-blog">
        <div class="container">
            <h2 class="section-heading"> {{ t('last_entries') }} </h2>
            <div class="row">
                <div v-for="p in blog_posts" class="col-md-3 col-sm-12">
                    <h3 v-if="$translate.current == 'es_ES'">{{ p.name_es }}</h3>
                    <h3 v-if="$translate.current == 'en_US'">{{ p.name }}</h3>

                    <p v-if="$translate.current == 'en_US'"> {{ p.intro }}</p>
                    <p v-if="$translate.current == 'es_ES'"> {{ p.intro_es }}</p>

                    <img :src="p.image" :alt="p.name" class="img_preview">
                    <router-link tag="a" :to="{ name: 'blog-post', params: { id: p.id} }" >
                        {{ t('read_more') }}
                    </router-link>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
     export default {
         props: ['blog_posts'],
         locales: {
            es_ES: {
                last_entries: 'Últimos artículos del blog',
                read_more: 'Leer todo el post'
            },
            en_US: {
                last_entries: 'Last post entries',
                read_more: 'Read the entire post'
            }
         }
     }
 </script>

<style scoped>
    .img_preview {
       max-width: 200px;
    }
</style>