<template>
     <div class="add-buttons">
         <a href="#" data-toggle="tooltip"
            data-placement="top"
            title="Add to cart"
            class="btn btn-skin btn-lg"
            @click.prevent="add_item_to_cart()"
            :class="{'disabled': is_button_disabled }"
         >
             <i class="fa fa-shopping-cart"></i> {{ t('add_cart') }}
         </a>
     </div>
</template>

<script>
    import { store } from '../../main'
    import { router } from '../../main'

    export default {
        name: 'shopping-cart-button',
        props:{
            'music_pack': { 'default': null },
            'music_track': { 'default': null },
        },
        computed: {
            is_music_pack() {
                return this.music_track === null;
            },
            selected_product(){
                return this.is_music_pack ? this.music_pack : this.music_track;
            },
            has_music_pack(){
                return this.music_pack !== null && store.state.music_packs_on_cart[this.music_pack.id] !== undefined;
            },
            has_music_track(){
                return this.music_track !== null && store.state.music_tracks_on_cart[this.music_track.id] !== undefined;
            },
            is_button_disabled(){
                return this.has_music_pack || this.has_music_track
            }
        },
        locales: {
            es_ES: { add_cart: 'Añadir al carro' },
            en_US: { add_cart: 'Add to cart' }
        },
        methods: {
            add_item_to_cart(){
                let vm = this;
                let swal_texts = { 'swal_title':'', 'text': '', 'confirm_button_text': '', 'cancel_button_text': '' };
                if(this.is_music_pack){
                    store.commit('add_music_pack_to_cart', {music_pack: vm.selected_product} );
                }else{
                    store.commit('add_music_track_to_cart', {music_track: vm.selected_product} );
                }

                if(this.$translate.current === 'en_US'){
                    swal_texts.title = 'Success';
                    swal_texts.text = 'You added ' + vm.selected_product.title + ' to your shopping cart. Do you want to continue shopping?';
                    swal_texts.confirm_button_text = 'Yes, I will add more items';
                    swal_texts.cancel_button_text = 'No, take me to checkout';
                }
                else{
                    swal_texts.title = 'Éxito';
                    swal_texts.text = 'Agregaste ' + vm.selected_product.title_es + ' a tu carro de compras. ¿Quieres continuar comprando?';
                    swal_texts.confirm_button_text = 'Sí, quiero agregar más productos';
                    swal_texts.cancel_button_text = 'No, llevarme al carro';
                }

                this.$swal({
                    title: swal_texts.title,
                    text: swal_texts.text,
                    type: 'success',
                    showCancelButton: true,
                    confirmButtonText: swal_texts.confirm_button_text,
                    cancelButtonText: swal_texts.cancel_button_text
                }).then(function() {
                    if(vm.is_music_pack){
                        router.push({name: 'music-packs'});
                    }else{
                        router.push({name: 'music-tracks'});
                    }


                }, function(dismiss) {
                     router.push({name: 'shopping-cart'});
                });
            }
        }
    }
</script>