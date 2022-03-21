<<<<<<< HEAD

<template>
  <v-app dark>
    <v-main>
      <v-container>
        <All_coffee />
      </v-container>
    </v-main>
  </v-app>
||||||| merged common ancestors
<template>
  <v-app dark>
    <v-main>
      <v-container>
        <Cafe_Creme />
      </v-container>
    </v-main>
  </v-app>
=======
<template lang="pug">
  v-app(dark)
    v-main
      Cafe
>>>>>>> f77fca8289ec0796530c3290b7ff5b8df0b9583e
</template>

<script>
<<<<<<< HEAD
import All_coffee from "../components/all_coffee.vue";
||||||| merged common ancestors
import Cafe_Creme from "../components/Cafe_Creme.vue";
=======
import Cafe from "../components/Cafe.vue";
>>>>>>> f77fca8289ec0796530c3290b7ff5b8df0b9583e
export default {
  data() {
    return {};
  },
<<<<<<< HEAD
  components: { All_coffee },
||||||| merged common ancestors
  components: { Cafe_Creme },
=======
  components: { Cafe },
>>>>>>> f77fca8289ec0796530c3290b7ff5b8df0b9583e
};
</script>