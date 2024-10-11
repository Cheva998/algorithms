
class CustomDate {
    date: Date;
    constructor(date: Date) {
        this.date = date
    }
    getCurrentYear(): number {
        return this.date.getFullYear()
    }
    getCurrentMonth(): number {
        return this.date.getMonth() + 1
    }
    getCurrentDate(): number {
        return this.date.getDate()
    }
}


function currentDates(): void {
    const newDate = new Date()
    const customDate = new CustomDate(newDate)
    console.log(customDate.getCurrentYear())
    console.log(customDate.getCurrentMonth())
    console.log(customDate.getCurrentDate())
}


currentDates()