import axios from 'axios';

const fetchData = () => {
    axios.get('/parked', response => {
        console.log(response);
        let parked = response.data.parked;
        let no_parked = response.data.no_parked;

        updateLayout(parked);
    });
};

const updateLayout = cars => {
    var ul = document.createElement('ul');
    ul.setAttribute('id','carList');

    cars = cars.map(car => car.license + '-' + car.parked + '-' + car.place_id);

    var t, tt;

    document.getElementById('parked').appendChild(ul);
    cars.forEach(renderCarList);

    function renderCarList(element, index, arr) {
        var li = document.createElement('li');

        ul.appendChild(li);

        t = document.createTextNode(element);

        li.innerHTML=li.innerHTML + element;
    }
}

setInterval(fetchData, 2000);