
<template>
  <v-app dark>
    <v-main>
      <v-container>
        <All_coffee />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import All_coffee from "../components/all_coffee.vue";
export default {
  data() {
    return {};
  },
  components: { All_coffee },
};
</script>