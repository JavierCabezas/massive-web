<template>
    <div class="container">
        <div class="breadcrumb-wrapper">
            <div class="container">
                <h1> {{ t('shopping_cart_title') }}</h1>
            </div>
        </div>

        <div v-if="!has_products">
            <h4 > {{ t('cart_without_products_1') }} </h4>
            <p> {{t('cart_without_products_2')}}</p>
            <ul>
                <li> <router-link tag="a" :to="{name: 'music-packs'}" > {{t('music_files')}} </router-link> </li>
                <li> <router-link tag="a" :to="{name: 'music-tracks'}" > {{t('music_packs')}} </router-link> </li>
            </ul>
        </div>
        <div v-else>
            <table class="table shopping-table">
                <thead>
                    <tr>
                        <td> {{ t('type') }} </td>
                        <td> {{ t('name') }} </td>
                        <td> {{ t('price') }} (USD) </td>
                        <td> {{ t('del') }} </td>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="mp in this.store.state.music_packs_on_cart">
                        <td> {{t('music_pack')}} </td>
                        <td v-if="$translate.current == 'en_US'"> {{ mp.title }} </td>
                        <td v-if="$translate.current == 'es_ES'"> {{ mp.title_es }}</td>
                        <td> {{ mp.price | cash }} </td>
                        <td> <a href="#" @click.prevent="remove_element('music_pack', mp.id)">
                                <span class="fa fa-remove"> </span>
                             </a>
                        </td>
                    </tr>

                    <tr class="shopping-total">
                        <td class="text" colspan="2">Total</td>
                        <td> {{ total_price() | cash }} </td>
                        <td> - </td>
                    </tr>
                </tbody>
            </table>

            <p class="shopping-info">
                {{ t('add_more') }}
                <router-link tag="a" :to="{name: 'music-tracks'}"> {{t('music_files')}} </router-link>
                {{t('or')}}
                <router-link tag="a" :to="{name: 'music-packs'}" > {{t('music_packs')}} </router-link>
             </p>
        </div>
    </div>
</template>

<script>
    import { store } from '../../main'
    import { router } from '../../main'

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
        created: function () {
            if(!store.state.is_logged_in){
                router.push({name: 'home'});
            }
        },
        filters: {
            cash: function (value) {
              const pieces = parseFloat(value).toFixed(2).split('');
              let ii = pieces.length - 3;
              while ((ii-=3) > 0) {
                pieces.splice(ii, 0, ',')
              }
              return "$" + pieces.join('')
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
                add_more: 'Si quieres agregar más productos al carro puedes revisar nuestras secciones de',
                or: 'o',
                name: 'Nombre',
                price: 'Precio',
                type: 'Tipo',
                del: 'Borrar'
            },
            en_US: {
                shopping_cart_title: 'My shopping cart',
                cart_without_products_1: 'You shopping cart is empty',
                cart_without_products_2: 'You may add:',
                music_packs: 'Music packs',
                music_files: 'Music files',
                music_pack: 'Music pack',
                music_file: 'Music file',
                add_more: 'If you want to add more products to the shopping cart to can check out our',
                or: 'or',
                name: 'Name',
                price: 'Price',
                type: 'Type',
                del: 'Delete'
            }
        },
        methods: {
            total_price: function(){
                var vm = this;
                var sum = 0;
                Object.keys(vm.store.state.music_packs_on_cart).forEach(function(idx) {
                      sum += vm.store.state.music_packs_on_cart[idx].price;
                });
                Object.keys(vm.store.state.music_tracks_on_cart).forEach(function(idx) {
                      sum += vm.store.state.music_tracks_on_cart[idx].price;
                });

                return sum;
            },
            remove_element: function(type, id){
                let swal_texts = { 'swal_title':'', 'text': '', 'confirm_button_text': '', 'cancel_button_text': '' };
                 if(this.$translate.current === 'en_US'){
                    swal_texts.title = 'Are you sure?';
                    swal_texts.text = 'This item will be deleted from the cart. Do you want to continue?';
                    swal_texts.confirm_button_text = 'Yes, delete it';
                    swal_texts.cancel_button_text = 'No, keep it';
                }
                else{
                    swal_texts.title = '¿Tienes seguridad?';
                    swal_texts.text = 'Se eliminará este objeto del carro. ¿Deseas continuar?';
                    swal_texts.confirm_button_text = 'Si, borrarlo';
                    swal_texts.cancel_button_text = 'No, conservarlo';
                }

                let vm = this;
                vm.$swal({
                    title: swal_texts.title,
                    text: swal_texts.text,
                    type: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: swal_texts.confirm_button_text,
                    cancelButtonText: swal_texts.cancel_button_text
                }).then(function () {
                    if(type==='music_pack'){
                        store.commit('remove_music_pack_from_cart', {music_pack_id: id} );
                    }else{
                        store.commit('remove_music_track_from_cart', {music_track_id: id} );
                    }
                    vm.$forceUpdate();
                });
            }
        }
    }
</script>