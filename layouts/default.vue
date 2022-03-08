<template>
  <v-app dark>
    <v-main>
      <v-container>
        <Espresso />
        <Cafe_Creme />
        <Cappuccino />
        <Easy_Clean />
        <Hot_Water />
        <Latte_Macchiato />
        <Milchschaum />
        <Warme_Milch />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Espresso from "../components/Espresso.vue"
import Cafe_Creme from "../components/Cafe_Creme.vue"
import Cappuccino from "../components/Cappuccino.vue"
import Easy_Clean from "../components/Easy_Clean.vue"
import Hot_Water from "../components/Hot_Water.vue"
import Latte_Macchiato from "../components/Latte_Macchiato.vue"
import Milchschaum from "../components/Milchschaum.vue"
import Warme_Milch from "../components/Warme_Milch.vue"
export default {
    data() {
        return {
        };
    },
    components: { Espresso, Cafe_Creme, Cappuccino, Easy_Clean, Hot_Water, Latte_Macchiato, Milchschaum, Warme_Milch }
}
</script>
