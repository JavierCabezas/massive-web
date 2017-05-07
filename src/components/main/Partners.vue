<template>
    <section class="partners">
        <div class="container">
            <h2 class="section-heading">Partners</h2>
            <ul class="partnerslider">
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
                <li><img src="../../img/partner.png"/></li>
            </ul>
        </div>
    </section>
</template>

<script>
    $(document).ready(function(){
        $(".partnerslider").bxSlider({
            slideWidth: 200,
            minSlides: 3,
            maxSlides: 6,
            slideMargin: 10,
            auto: true
        });
    });
</script>