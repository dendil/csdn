#!/bin/bash
function Send_wechat(){
	local Corpid="wwe0c2d77a28f790c7"
	local Corpsecret="GNx-afsJ29QQQhJL_-i1npOMm4O7CoHsgN0va0AXzW4"
	local Jna_Secret="GNx-afsJ29QQQhJL_-i1npOMm4O7CoHsgN0va0AXzW4"
	local Access_token_file="/tmp/access_token"

	local Gettoken_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
	local Message_send_url="https://qyapi.weixin.qq.com/cgi-bin/message/send"

	if [ -f ${Access_token_file} ];then
		local	Access_token=`cat ${Access_token_file} |xargs echo |awk -F"[ ,:]"  '{print $6}'`
	else
		local Access_token=``
	fi
function Get_access_token(){
	/usr/bin/curl   ${Gettoken_url}?corpid=${Corpid}\&corpsecret=${Corpsecret} -o ${Access_token_file}
	echo `date +%s` >> ${Access_token_file}
	Access_token=`cat ${Access_token_file} |xargs echo |awk -F"[ ,:]"  '{print $6}'`
	echo ${Access_token}
}

function Check_access_token(){
	Access_token_time=`awk -F"[ ,:}]"  '{print $9}' ${Access_token_file}`
	local Now_time=`date +%s`
	if [ ${Access_token} == "" ] ;then
		Get_access_token
	fi
	if [  "${Access_token_time}"x != ""x ];then
		Check_time=$((${Now_time}-${Access_token_time}))
	fi
	if [ "${Access_token_time}"x == ""x ]; then
		Get_access_token
	fi
	if [ ! "${Check_time}"x == ""x ] ;then
		if [ ${Check_time} -ge 7200 ] ;then
			Get_access_token
		fi
	fi
}
	Check_access_token

Data="{\
\"touser\" : \"@all\",\
\"toparty\" : \"PartyID1|PartyID2\",\
\"totag\" : \"TagID1 | TagID2\",\
\"msgtype\" : \"text\",\
\"agentid\" : 1000004,\
\"text\" : {\
	\"content\" : \"$1\"},\
	\"safe\":0\
}"
	curl -H "Content-Type:application/json"  -X POST --data  "${Data}"  ${Message_send_url}?access_token=${Access_token}
}