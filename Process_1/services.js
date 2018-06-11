var mongo = require('mongodb');
var Server = mongo.Server,
    Db = mongo.Db,
    BSON = mongo.BSONPure;
var ObjectID = require('mongodb').ObjectID;
var empIdGenerator = require('randomstring');
var EmpID;

var server = new Server('localhost', 27017, {auto_reconnect: true});
db = new Db('HRM', server);

db.open(function (err, db) {
    if (!err) {
        console.log("Connected to 'HRM' database");

    }
    else {
        console.log("Error while connecting to 'HRM' database");
    }
});



exports.getAccessLog = function (req, res) {

    var data = req.body;
    var content;

    fs.readFile('./accessLogs', { encoding: 'utf8' },function read(err, data){
        if (err) {
            throw err;
        }
        content = data;
        processFile();          // Or put the next step in a function and invoke it
    });

    function processFile() {
        console.log(content);
        var lines, i;
        var result = [];

        lines = (content).split("\n");
        for(i = 0; i < lines.length - 1; i++)
        {
            try {

            }
            catch (e) {
                e.pri
            }
            var objectValue = JSON.parse(lines[i].replace("\\",""));
            var timeStamp = objectValue.timestamp;

            var req = objectValue.req;
            var url = req.url;


            console.log("URL : " +url);

            var dateTimestamp =  timeStamp.split('T')[0]
            //console.log("TimeStamp : " +dateTimestamp);

            var today = new Date();
            var todaysDate = convert(today);
            var yesterday = new Date();
            yesterday.setDate(today.getDate()-1);

            var yesterdayDate = convert(yesterday);

            //console.log("TimeStamp : " +dateTimestamp);
            //console.log("yesterdayDate : " + yesterdayDate);
            //console.log("todaysDate : " + todaysDate);
//new Date(dateTimestamp) == new Date(todaysDate) ||
            if( dateTimestamp == yesterdayDate || dateTimestamp == todaysDate)
            {
                //console.log("yesterdayDate : " + yesterday);
                //console.log("todaysDate : " + todaysDate);
                //console.log("Push Happens");
                if(url != "/getAccessLog")
                {
                    result.push(JSON.parse(lines[i]));
                }
            }

           // console.log("responce : " + lines[i]);
        }

        var date = new Date();
       // var dateString = timeSolver.getString(date, "YYYY-MM-DD");
       // console.log("date string : " + dateString);
       // newD = dateFormat(today, "YYYY-MM-DD HH:MM:SS");


        res.contentType('application/json');
        res.send(result);

      //  last = lines[i];
    }

    function convert(str) {
        var date = new Date(str),
            mnth = ("0" + (date.getMonth()+1)).slice(-2),
            day  = ("0" + date.getDate()).slice(-2);
        return [ date.getFullYear(), mnth, day ].join("-");
    }
};