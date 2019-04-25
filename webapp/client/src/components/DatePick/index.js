import React from "react";
import ReactDOM from "react-dom";

import "react-dates/initialize";
import { SingleDatePicker } from "react-dates";
import moment from "moment";
import "react-dates/lib/css/_datepicker.css";


class DatePick extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: moment(),
      focused: false,
      string: "test"
    };
  }
  handleDateChange = (date) => {
    this.setState({ date })
    this.props.onDateSelect(date.format("YYYY-MM-DD")); 
     
    this.props.netWorkCall(date.format("YYYY-MM-DD")); 
          
}
  render() {
    return (
      <div style={{  }}>
        <SingleDatePicker
           showDefaultInputIcon = {true}
          date={this.state.date} // momentPropTypes.momentObj or null
          onDateChange={this.handleDateChange} 
          focused={this.state.focused} // PropTypes.bool
          onFocusChange={({ focused }) => this.setState({ focused })} // PropTypes.func.isRequired
          numberOfMonths={1}
          displayFormat="YYYY-MM-DD"
          readOnly
          isOutsideRange={() => false}

          // renderDayContents={(day) => (day.day() % 6 === 5 ? '😻' : day.format('D'))}
          
        />
        {/* Selected date is {this.state.date.format("YYYY-MM-DD")} */}
        
      </div>
    );
  }
}

export default DatePick
