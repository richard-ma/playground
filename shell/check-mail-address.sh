#!/bin/bash
checkmailaddress() {
    # check mail address
    if [ $1 ]; then
       MAIL=`echo $1|tr -d '\r'` # tr will delete the \r and use \n
    else
       echo "pls input mail address"
       return 1
    fi
  
    echo "START CHECK ${MAIL}"
    # get domain
    HOST=`echo ${MAIL} | awk -F @ '{print $2}'` # awk to cut the second part of mail address
  
    echo "START FIND MAIL SERVER: ${HOST}"
    # check mail server
    MAILHOST=`nslookup -q=mx ${HOST} | grep 'mail exchanger' | line | awk '{print $6}' | sed 's/\.$//'`
    # nslookup -q=mx $HOST => get all mx record of domain
    # grep 'mail exchanger' => get mail exchanger server domain
    # line => one line for result set
    # awk '{print $6}' => get mail server domain
    # sed 's/\./$//' => delete domain last . character
    if [ ! ${MAILHOST} ]; then
        MAILHOST=`nslookup -q=mx $HOST|grep "mail addr"|line|awk '{print $4}'`
        # keyword maybe mail addr
    fi

    # NOT found mail server
    if [ ! ${MAILHOST} ]; then
        echo "NOT FIND MAIL SERVER ${HOST}"
        return 1
    fi
    echo "FIND MAIL SERVER: ${MAILHOST}"

    # send SMTP message
    SMTP=`echo -e "HELO gmail.com\nMAIL FROM: <test@gmail.com>\nRCPT TO: <$MAIL>\nQUIT\n"  |nc -q10 -w60 ${MAILHOST} 25`
    # --SMTP message
    #
    # HELO gmail.com\n
    # MAIL FROM: <test@gmail.com>\n
    # RCPT TO: <$MAIL>\n
    # QUIT\n"
    #
    # nc -q10 -w60 ${MAILHOST} 25 => send SMTP message to mail server port 25
    for CODE in 500 510 502 503 504 521 530 550 551 552 553 554 
    do
        CHECK=`echo ${SMTP}|grep '${CODE}'`
        if [ ${CHECK} ]; then
            echo "ERROR ${CHECK}"
            return 1
        fi
    done
    echo "CHECK ${MAIL} OK"
    return 0
}

echo -n > "mail_ok.txt"
echo -n > "mail_error.txt"

# mail.txt format like:
# username@example.com
for i in `cat mail.txt`
do
    checkmailaddress $i
    result=$?
    if [ ${result} -eq 0 ]; then
        echo "$i" >> "mail_ok.txt"
    else
        echo "$i" >> "mail_error.txt"
    fi
done

