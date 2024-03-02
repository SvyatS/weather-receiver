import {useState, useEffect} from 'react'

import './App.css'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import {faker} from '@faker-js/faker';
import {getCurrentTemperature} from './api'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

let options1 = {
  responsive: true,
  plugins: {
    legend: {
      display: false
    },
    title: {
      display: true,
      text: 'Temperature',
    },
  },
};

let options2 = JSON.parse(JSON.stringify(options1))
options2.plugins.title.text = 'Average hour temperature'

let options3 = JSON.parse(JSON.stringify(options1))
options3.plugins.title.text = 'Average day temperature'

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

export const data1 = {
  labels,
  datasets: [
    {
      data: labels.map(() => faker.number.int({ min: -10, max: 10 })),
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
  ],
};

export const data2 = {
  labels,
  datasets: [
    {
      data: labels.map(() => faker.number.int({ min: -10, max: 10 })),
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
  ],
};

export const data3 = {
  labels,
  datasets: [
    {
      data: labels.map(() => faker.number.int({ min: -10, max: 0 })),
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
  ],
};
let data = {
  labels: [],
  values: []
}

function App() {
  const [temperature, setTemperature] = useState([]);
  const [currentTemperature, setCurrentTemperature] = useState('');
  const [avgHour, setAvgHour] = useState([]);
  const [avgDay, setAvgDay] = useState([]);

  const getCurrentTemperature = () => {
    fetch(`http://127.0.0.1:8000/api/v1/weather/`)
       .then((response) => response.json())
       .then((data) => {
          setTemperature(data)
          setCurrentTemperature(data.slice(-1)[0]?.temperature)
       })
    .catch((err) => {
       console.log(err.message);
    });
  };

  const getAvgHourTemperature = () => {
    fetch(`http://127.0.0.1:8000/api/v1/avg-weather-by-hour/`)
       .then((response) => response.json())
       .then((data) => {
          setAvgHour(data)
       })
    .catch((err) => {
       console.log(err.message);
    });
  };

  const getAvgDayTemperature = () => {
    fetch(`http://127.0.0.1:8000/api/v1/avg-weather-by-day/`)
       .then((response) => response.json())
       .then((data) => {
          setAvgDay(data)
       })
    .catch((err) => {
       console.log(err.message);
    });
  };

  

  useEffect(() => {
    getCurrentTemperature()
    getAvgHourTemperature()
    getAvgDayTemperature()
  }, [])
  
  
  return (
    <>
      <div>
        <h3>Current temperature: { currentTemperature }</h3>
        <Line 
          options={options1} 
          data= {
            {
              labels: temperature.map(({created_at}) => created_at),
              datasets: [
                {
                  data: temperature.map(({temperature}) => temperature)
                }
              ]
            }
          }
        />
        <Line
          options={options2}
          data= {
              {
                labels: avgHour.map(({created_at}) => created_at),
                datasets: [
                  {
                    data: avgHour.map(({temperature}) => temperature)
                  }
                ]
              }
            } 
          />
        <Line 
          options={options3} 
          data= {
              {
                labels: avgDay.map(({created_at}) => created_at),
                datasets: [
                  {
                    data: avgDay.map(({temperature}) => temperature)
                  }
                ]
              }
            } 
          />
      </div>
    </>
  )
}

export default App
