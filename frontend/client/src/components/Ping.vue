<template>
    <div>
        <div>
            <p>{{ msg }}</p>
        </div>
        <div>
            <form id="">
                <div class="row">
                    <label class="col-form-label col-form-label-lg">Nombre </label>
                    <input type="text" class="form-control">
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Email </label>
                    <input type="email" class="form-control">
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Edad </label>
                    <select name="" id="">
                        <option value="">18-25 years</option>
                        <option value="">26-33 years</option>
                        <option value="">34-40 years</option>
                        <option value="">40+ years</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Tiempo promedio al dia en Tiktok </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Tiempo promedio al dia en WhatsApp </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Tiempo promedio al dia en Twitter </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Tiempo promedio al dia en Instagram </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                </div>
                <div>
                    <label class="col-form-label col-form-label-lg">Tiempo promedio al dia en Facebook </label>
                    <select name="" id="">
                        <option value="">0</option>
                        <option value="">1</option>
                        <option value="">2</option>
                        <option value="">3</option>
                        <option value="">4</option>
                        <option value="">5</option>
                        <option value="">6</option>
                        <option value="">7</option>
                        <option value="">8</option>
                        <option value="">9</option>
                        <option value="">10</option>
                    </select>
                <div class="col-12 form-group text-center">
                    <button class="btn vue-bg btn-lg col-4">Cargar</button>
                </div>
                </div>
            </form>
        </div>
        

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style>
.vue-bg{
    background-color: rgba(111, 207, 224, 0.705);
}
</style>

