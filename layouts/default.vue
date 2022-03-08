<template>
  <v-app dark>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Milchkaffe from "../components/Milchkaffe.vue"
export default {
    data() {
        return {
        };
    },
    components: { Milchkaffe }
}
</script>
