createCharts();

async function createCharts() {
  const res = await fetch('charts');
  const chartsData = await res.json();

  if ('value_chart' in chartsData)
    renderCharts(chartsData);
  else
    renderPlaceholder();
}

function renderCharts(chartsData) {
  const { value_chart, expense_chart, savings_chart } = chartsData;
  renderLineChart(value_chart);
  renderPieChart(expense_chart);
  renderBarChart(savings_chart);
}

function renderPlaceholder() {
  const container = document.querySelector('.placeholder');
  container.innerHTML = `
    <p>You have no transactions yet in your portfolio</p>
    <p>
      Start adding
      <a class="link" href="/transactions">
        transactions</a>
      now
    </p>
  `;
}

function renderLineChart(data) {
  const options = {
    chart: {
      type: 'area',
      height: '350px',
      foreColor: '#ffffff',
      toolbar: { show: false }
    },
    fill: {
      colors: ['#7a4bdf'],
      gradient: {
        shadeIntensity: 0,
        opacityFrom: .7,
        opacityTo: .4,
        stops: [0, 100]
      }
    },
    series: [{
      name: 'Value',
      data: data.map(dataPoint => dataPoint.value)
    }],
    xaxis: {
      name: 'Date',
      labels: { show: false },
      categories: data.map(dataPoint => dataPoint.date),
      axisTicks: { show: false },
      axisBorder: { show: false }
    },
    yaxis: {
      min: 0,
      labels: { formatter: currencyFormater }
    },
    tooltip: {
      theme: 'dark',
      y: { formatter: currencyFormater }
    },
    title: { text: 'Total Value Over Time' },
    grid: { borderColor: '#c3c3c320' },
    stroke: { width: 2 },
    dataLabels: { enabled: false }
  }

  const chartContainer = document.getElementById('value_chart');
  const chart = new ApexCharts(chartContainer, options);
  chart.render();
}

function renderPieChart(data) {
  const options = {
    chart: {
      type: 'donut',
      height: '320px',
      foreColor: '#ffffff'
    },
    plotOptions: {
      pie: {
        donut: {
          size: '70%',
          labels: {
            show: true,
            value: { formatter: currencyFormater }
          }
        }
      }
    },
    stroke: {
      show: false
    },
    series: Object.values(data).map(val => Number(val)),
    labels: Object.keys(data),
    title: { text: 'Cumulative Expenses by Category' },
    tooltip: {
      enabled: false
    }
  }

  const chartContainer = document.getElementById('pie_chart');
  const chart = new ApexCharts(chartContainer, options);
  chart.render();
}

function renderBarChart(data) {
  const options = {
    chart: {
      type: 'bar',
      foreColor: '#ffffff',
      toolbar: { show: false }
    },
    plotOptions: { bar: { columnWidth: '50%' } },
    series: [
      {
        name: 'Income',
        data: data.income,
      },
      {
        name: 'Expenses',
        data: data.expenses,
      }
    ],
    xaxis: {
      categories: data.months,
      title: { text: 'Month' }
    },
    yaxis: {
      title: { text: 'Amount ($)' }
    },
    tooltip: {
      theme: 'dark',
      y: { formatter: currencyFormater }
    },
    colors: ['#00E396', '#FF4560'],
    grid: { borderColor: '#c3c3c320' },
    legend: { position: 'top' },
    title: { text: 'Monthly Income VS Expenses (last 6 months)' }
  };

  const chartContainer = document.getElementById('bar_chart');
  const chart = new ApexCharts(chartContainer, options);
  chart.render();
}

function currencyFormater(value) {
  if (typeof value === 'number')
    return '$' + value.toFixed(2);

  if (typeof value === 'string')
    return '$' + value;
}