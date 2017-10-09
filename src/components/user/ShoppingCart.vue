<template>
    <div class="container">
        <h1> {{ t('shopping_cart_title') }} </h1>

        <div v-if="!has_products">
            <h4 > {{ t('cart_without_products_1') }} </h4>
            <p> {{t('cart_without_products_2')}}</p>
            <ul>
                <li> <router-link tag="a" :to="{name: 'music-packs'}" > {{t('music_files')}} </router-link> </li>
                <li> <router-link tag="a" :to="{name: 'music-tracks'}" > {{t('music_packs')}} </router-link> </li>
            </ul>
        </div>
        <div v-else>
            <table class="table">
                <thead>
                    <tr>
                        <td> {{ t('type') }} </td>
                        <td> {{ t('name') }} </td>
                        <td> {{ t('price') }} </td>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="mp in this.store.state.music_packs_on_cart">
                        <td> {{t('music_pack')}} </td>
                        <td> {{ mp }} </td>
                        <td> {{ mp.price }} </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    import { store } from '../../main'

    export default {
        data () {
            return {
                store: store
            }
        },
        computed: {
            has_music_packs(){
                return Object.keys(store.state.music_packs_on_cart).length > 0;
            },
            has_music_tracks(){
                return Object.keys(store.state.music_tracks_on_cart).length > 0;
            },
            has_products(){
                return this.has_music_packs || this.has_music_tracks;
            }
        },
        locales: {
            es_ES: {
                shopping_cart_title: 'Mi carro de compras',
                cart_without_products_1: 'Tu carro de compras se encuentra vacío',
                cart_without_products_2: 'Puedes agregar:',
                music_packs: 'Packs de música',
                music_files: 'Canciones sueltas',
                music_pack: 'Pack de música',
                music_file: 'Canción suelta',
                name: 'Nombre',
                price: 'Precio',
                type: 'Tipo'
            },
            en_US: {
                shopping_cart_title: 'My shopping cart',
                cart_without_products_1: 'You shopping cart is empty',
                cart_without_products_2: 'You may add:',
                music_packs: 'Music packs',
                music_files: 'Music files',
                music_pack: 'Music pack',
                music_file: 'Music file',
                name: 'Name',
                price: 'Price',
                type: 'Type'
            }
        },
        methods: {

        }
    }
</script>