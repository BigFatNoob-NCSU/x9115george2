import os, sys
sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True
from template import *
__author__ = 'george'

N = Many()

n1 = N + SoftGoal(
  "Increase Resources[Services]",
  container = "CS"
)

n2 = N + HardGoal(
  "Services be Bilingual",
  container = "CS"
)

n3 = N + SoftGoal(
  "High Quality Service",
  container = "CS"
)

n4 = N + Task(
  "Maintain/Implement CS Services",
  container = "CS"
)

n5 = N + Task(
  "Maintain Web Services",
  container = "CS"
)

n6 = N + Task(
  "Maintain Phone Services",
  container = "CS"
)

n7 = N + Task(
  "Maintain/Implement PHL Services",
  container = "CS"
)

n8 = N + SoftGoal(
  "Increase Number of Services",
  container = "CS"
)

n9 = N + SoftGoal(
  "Efficient Services",
  container = "CS"
)

n10 = N + SoftGoal(
  "Available [Services]",
  container = "CS"
)

n11 = N + Resource(
  "Service Resources",
  container = "CS"
)

n12 = N + SoftGoal(
  "Measure Success of Services",
  container = "CS"
)

n13 = N + SoftGoal(
  "Immediacy",
  container = "CS Technology Services"
)

n14 = N + HardGoal(
  "Services Be Bilingual",
  container = "CS Technology Services"
)

n15 = N + SoftGoal(
  "Increase Resources [Services]",
  container = "CS Technology Services"
)

n16 = N + SoftGoal(
  "Anonymity",
  container = "CS Technology Services"
)

n17 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "CS Technology Services"
)

n18 = N + SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS Technology Services"
)

n19 = N + SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Technology Services"
)

n20 = N + SoftGoal(
  "Increase Web Resources",
  container = "CS Technology Services"
)

n21 = N + SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "CS Technology Services"
)

n22 = N + SoftGoal(
  "Increased Web Services",
  container = "CS Technology Services"
)

n23 = N + SoftGoal(
  "Avoid Bad Advice",
  container = "CS Technology Services"
)

n24 = N + SoftGoal(
  "Direct Response to Kids",
  container = "CS Technology Services"
)

n25 = N + SoftGoal(
  "Improve Website Content",
  container = "CS Technology Services"
)

n26 = N + SoftGoal(
  "Efficient Web Services",
  container = "CS Technology Services"
)

n27 = N + SoftGoal(
  "Decrease Response Time",
  container = "CS Technology Services"
)

n28 = N + SoftGoal(
  "Increase Phone Resources",
  container = "CS Technology Services"
)

n29 = N + Task(
  "Maintain Phone Services",
  container = "CS Technology Services"
)

n30 = N + SoftGoal(
  "Available [Services]",
  container = "CS Technology Services"
)

n31 = N + Task(
  "Implement Phone Feedback",
  container = "CS Technology Services"
)

n32 = N + HardGoal(
  "Counsellors be Professionally Trained",
  container = "CS Technology Services"
)

n33 = N + Task(
  "Acquire Feedback",
  container = "CS Technology Services"
)

n34 = N + HardGoal(
  "Service Levels Be Met",
  container = "CS Technology Services"
)

n35 = N + SoftGoal(
  "Increase Number of Services",
  container = "CS Technology Services"
)

n36 = N + SoftGoal(
  "High Quality Services",
  container = "CS Technology Services"
)

n37 = N + SoftGoal(
  "Efficient Services",
  container = "CS Technology Services"
)

n38 = N + SoftGoal(
  "Confidentiality",
  container = "CS Technology Services"
)

n39 = N + SoftGoal(
  "Relevance in Kids Lives",
  container = "CS Technology Services"
)

n40 = N + SoftGoal(
  "Efficient Phone Services",
  container = "CS Technology Services"
)

n41 = N + SoftGoal(
  "Anonymity [Parents]",
  container = "CS Technology Services"
)

n42 = N + SoftGoal(
  "Confidentiality [Parents]",
  container = "CS Technology Services"
)

n43 = N + Task(
  "Implement Services",
  container = "CS Technology Services"
)

n44 = N + HardGoal(
  "Services be provided for Kids Bullying Line",
  container = "CS Technology Services"
)

n45 = N + Task(
  "Implement Feedback Collection",
  container = "CS Technology Services"
)

n46 = N + SoftGoal(
  "Connect Back to the Community",
  container = "CS Technology Services"
)

n47 = N + SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Technology Services"
)

n48 = N + Task(
  "Maintain/Implement CS Services",
  container = "CS Technology Services"
)

n49 = N + Task(
  "Maintain Web Services",
  container = "CS Technology Services"
)

n50 = N + Task(
  "Acquire Service Resources",
  container = "CS Technology Services"
)

n51 = N + Task(
  "Implement Feedback Form",
  container = "CS Technology Services"
)

n52 = N + Task(
  "Maintain/Implement PHL Services",
  container = "CS Technology Services"
)

n53 = N + HardGoal(
  "Services be provided for Kids Bullying Line",
  container = "Provincial government"
)

n54 = N + SoftGoal(
  "Quality [Services]",
  container = "Parents"
)

n55 = N + SoftGoal(
  "Immediacy [Services]",
  container = "Parents"
)

n56 = N + SoftGoal(
  "Confidentiality [Services]",
  container = "Parents"
)

n57 = N + SoftGoal(
  "Connect Back to the Community",
  container = "Parents"
)

n58 = N + SoftGoal(
  "Availability [Services]",
  container = "Parents"
)

n59 = N + SoftGoal(
  "Improve Image to Kids",
  container = "CS"
)

n60 = N + SoftGoal(
  "Maintain Services above Competition",
  container = "CS"
)

n61 = N + SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS"
)

n62 = N + SoftGoal(
  "Reduce Contagion Effect [Of Harmful Actions]",
  container = "CS"
)

n63 = N + SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  container = "CS"
)

n64 = N + SoftGoal(
  "Web Services Self Serve",
  container = "CS"
)

n65 = N + SoftGoal(
  "Empowering Kids to Help Themselves",
  container = "CS"
)

n66 = N + Resource(
  "Web Server",
  container = "IT Department"
)

n67 = N + Resource(
  "Feedback Form Software",
  container = "IT Department"
)

n68 = N + Resource(
  "Web Software",
  container = "IT Department"
)

n69 = N + HardGoal(
  "Telephony Be Implemented and Managed",
  container = "IT Department"
)

n70 = N + Task(
  "Implement Phone Feedback",
  container = "IT Department"
)

n71 = N + Task(
  "Put Content Onto Website",
  container = "IT Department"
)

n72 = N + Resource(
  "Strategic Blue Print",
  container = "Web Task Force"
)

n73 = N + Task(
  "Maintain Implement CS Services",
  container = "CS Service"
)

n74 = N + SoftGoal(
  "Connect Back to the Community",
  container = "CS Service"
)

n75 = N + Task(
  "Maintain Implement CS Web Services",
  container = "CS Service"
)

n76 = N + Task(
  "Maintain CS Phone Services",
  container = "CS Service"
)

n77 = N + SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Service"
)

n78 = N + Task(
  "Maintain/Implement CS Services",
)

n79 = N + SoftGoal(
  "Connect Back to the Community",
)

n80 = N + SoftGoal(
  "Kids Have Ownership of Services",
)

n81 = N + SoftGoal(
  "Web Services Self Serve",
  container = "CS Web Services"
)

n82 = N + SoftGoal(
  "Web Services Self Serve",
)

n83 = N + Task(
  "Maintain/Implement CS Web Services",
)

n84 = N + SoftGoal(
  "Immediacy",
)

n85 = N + SoftGoal(
  "Easier Navigation [CS Web Services]",
)

n86 = N + SoftGoal(
  "Decrease Response Time",
)

n87 = N + SoftGoal(
  "Measure Success of Services",
)

n88 = N + SoftGoal(
  "Sufficiently Moderated Web Services",
)

n89 = N + Task(
  "Implement Feedback Form",
  container = "Web Service"
)

n90 = N + Task(
  "Obtain Needed Software",
  container = "Web Service"
)

n91 = N + Task(
  "Obtain Web Server",
  container = "Web Service"
)

n92 = N + SoftGoal(
  "Web Services Self Serve",
  container = "Web Service"
)

n93 = N + SoftGoal(
  "Immediacy",
  container = "Web Service"
)

n94 = N + HardGoal(
  "Only Online Request from Canadians Accepted",
  container = "Web Service"
)

n95 = N + SoftGoal(
  "Decrease Response Time",
  container = "Web Service"
)

n96 = N + SoftGoal(
  "Control [Web Services]",
  container = "Web Service"
)

n97 = N + Task(
  "Maintain PHL Web Services",
  container = "Web Service"
)

n98 = N + SoftGoal(
  "Available [Services]",
  container = "Web Service"
)

n99 = N + SoftGoal(
  "Efficient Web Services",
  container = "Web Service"
)

n100 = N + SoftGoal(
  "Improve Website Content",
  container = "Web Service"
)

n101 = N + SoftGoal(
  "Avoid Bad Advice",
  container = "Web Service"
)

n102 = N + SoftGoal(
  "Increased Web Services",
  container = "Web Service"
)

n103 = N + SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "Web Service"
)

n104 = N + SoftGoal(
  "Confidentiality [Kids]",
  container = "Web Service"
)

n105 = N + SoftGoal(
  "Increase Web Resources",
  container = "Web Service"
)

n106 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "Web Service"
)

n107 = N + SoftGoal(
  "Measure Success of Services",
  container = "Web Service"
)

n108 = N + SoftGoal(
  "Accommodate Web Site Traffic",
  container = "Web Service"
)

n109 = N + Task(
  "Maintain Web Services",
  container = "Web Service"
)

n110 = N + HardGoal(
  "Web Traffic Be Kept Track of",
  container = "Web Service"
)

n111 = N + Task(
  "Maintain/Implement CS Web Services",
  container = "Web Service"
)

n112 = N + HardGoal(
  "Web Site Content Be Updated Daily",
  container = "Web Service"
)

n113 = N + Task(
  "Obtain Software",
  container = "Web Service"
)

n114 = N + SoftGoal(
  "Sufficient Counselling Resources",
  container = "Web Service"
)

n115 = N + SoftGoal(
  "Easier Navigation [CS Web Services]",
  container = "Web Service"
)

n116 = N + SoftGoal(
  "Anonymity [Kids]",
)

n117 = N + SoftGoal(
  "Kids Have Ownership of Services",
)

n118 = N + SoftGoal(
  "Confidentiality [Kids]",
)

n119 = N + SoftGoal(
  "Increase Web Resources",
)

n120 = N + SoftGoal(
  "Sufficiently Moderated Web Services",
)

n121 = N + SoftGoal(
  "Increased Web Services",
)

n122 = N + SoftGoal(
  "Avoid Bad Advice",
)

n123 = N + Task(
  "Maintain Web Services",
)

n124 = N + Task(
  "Implement Feedback Form",
)

n125 = N + SoftGoal(
  "Improve Website Content",
)

n126 = N + SoftGoal(
  "Efficient Web Services",
)

n127 = N + SoftGoal(
  "Decrease Response Time",
)

n128 = N + SoftGoal(
  "Connect Back to the Community",
)

n129 = N + SoftGoal(
  "Available [Services]",
)

n130 = N + SoftGoal(
  "Relevance in Kids Lives",
)

n131 = N + SoftGoal(
  "Increased Web Services"
)

n132 = N + SoftGoal(
  "Sufficient Counselling Resources"
)

n133 = N + SoftGoal(
  "Anonymity [Kids]"
)

n134 = N + SoftGoal(
  "Control [Web Services]"
)

n135 = N + SoftGoal(
  "Direct Response to Kids"
)

n136 = N + SoftGoal(
  "Confidentiality [Kids]"
)

n137 = N + SoftGoal(
  "Avoid Bad Advice"
)

n138 = N + Task(
  "Maintain CS Phone Services"
)

n139 = N + SoftGoal(
  "Immediacy",
  container = "PHL Web Service -> Web Service"
)

n140 = N + SoftGoal(
  "Immediacy",
  container = "Phone Service -> Web Service"
)

n141 = N + SoftGoal(
  "Increase Phone Resources",
)

n142 = N + SoftGoal(
  "Efficient Phone Services",
)

n143 = N + SoftGoal(
  "Anonymity [Parents]",
)

n145 = N + Task(
  "Maintain Phone Services",
)

n146 = N + SoftGoal(
  "Confidentiality [Parents]",
)

n147 = N + Task(
  "Implement Phone Feedback",
)

n148 = N + HardGoal(
  "Counsellors Be Professionally Trained",
  container = "Counselling Management"
)

n149 = N + Resource(
  "Feedback",
  container = "Parents"
)

n150 = N + SoftGoal(
  "Anonymity [Parents]",
  container = "Parents"
)

n151 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "PHL Web Services"
)

n152 = N + SoftGoal(
  "Confidentiality [Parents]",
)

n153 = N + SoftGoal(
  "Connect Back to the Community",
)

n154 = N + Task(
  "Maintain PHL Web Services",
)

n155 = N + Task(
  "Maintain PHL Phone Services",
)

n156 = N + Task(
  "Maintain PHL Phone Services",
  container = "Parents"
)

n157 = N + Task(
  "Parents use Phone Counselling",
  container = "Parents"
)

n158 = N + SoftGoal(
  "Similarity with other parents' problems",
  container = "Parents"
)

n159 = N + SoftGoal(
  "Decrease [Phone Waiting Time]",
  container = "Parents"
)

n160 = N + SoftGoal(
  "Immediacy",
  container = "Phone Service"
)

n161 = N + SoftGoal(
  "Increase Phone Resources",
  container = "Phone Service"
)

n162 = N + SoftGoal(
  "Available [Services]",
  container = "Phone Service"
)

n163 = N + SoftGoal(
  "Sufficient Counselling Resources",
  container = "Phone Service"
)

n164 = N + Task(
  "Maintain CS Phone Services",
  container = "Phone Service"
)

n165 = N + SoftGoal(
  "Anonymity [Parents]",
  container = "Phone Service"
)

n166 = N + Task(
  "Maintain PHL Phone Services",
  container = "Phone Service"
)

n167 = N + SoftGoal(
  "Accommodate Phone Traffic",
  container = "Phone Service"
)

n168 = N + Task(
  "Implement Phone Feedback",
  container = "Phone Service"
)

n169 = N + SoftGoal(
  "Measure Success of Services",
  container = "Phone Service"
)

n170 = N + SoftGoal(
  "Confidentiality [Parents]",
  container = "Phone Service"
)

n171 = N + SoftGoal(
  "Efficient Phone Services",
  container = "Phone Service"
)

n172 = N + Task(
  "Maintain Phone Services",
  container = "Phone Service"
)

n173 = N + Task(
  "Trace Calls",
  container = "Phone Service"
)

n174 = N + HardGoal(
  "Telephony Be Implemented and Managed",
  container = "Phone Service"
)

n175 = N + SoftGoal(
  "Connect Back to the Community",
  container = "PHL Service"
)

n176 = N + Task(
  "Maintain/Implement PHL Services",
  container = "PHL Service"
)

n177 = N + Task(
  "Maintain PHL Web Services",
  container = "PHL Service"
)

n178 = N + Task(
  "Maintain PHL Phone Services",
  container = "PHL Service"
)

n179 = N + Task(
  "Kids Read General Questions and Answers",
  container = "Kids and Youth"
)

n180 = N + Task(
  "Implement Polls about Kids",
  container = "Kids and Youth"
)

n181 = N + Task(
  "Kids read Polls about Kids",
  container = "Kids and Youth"
)

n182 = N + Task(
  "Implement General Questions and Answers",
  container = "Kids and Youth"
)

n183 = N + Task(
  "Kids use get Informed Section of Website",
  container = "Kids and Youth"
)

n184 = N + Task(
  "Implement Get Informed Section of Web Site",
  container = "Kids and Youth"
)

n185 = N + SoftGoal(
  "Increase Emphasis on Online Feedback Form",
  container = "Counselling"
)

n186 = N + SoftGoal(
  "Easier to Find Posts [Web Posting Technology]",
  container = "Counselling"
)

n187 = N + Resource(
  "Web Site Content",
  container = "Counselling"
)

n188 = N + SoftGoal(
  "Anonymity [Counsellors]",
  container = "Counselling"
)

n189 = N + SoftGoal(
  "Reduce Prank Calls ",
  container = "Counselling"
)

n190 = N + SoftGoal(
  "Avoid Dialogues",
  container = "Counselling"
)

n191 = N + SoftGoal(
  "Correct Interpretation of Counsel",
  container = "Counselling"
)

n192 = N + SoftGoal(
  "Reduce Number of Steps [Web Posting Technology]",
  container = "Counselling"
)

n193 = N + SoftGoal(
  "Control of Counselling Work",
  container = "Counselling"
)

n194 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "CS Web Services"
)

n195 = N + Task(
  "Maintain/Implement CS Web Services",
  container = "CS Web Services"
)

n196 = N + SoftGoal(
  "Relevance in Kids Lives",
  container = "CS Web Services"
)

n197 = N + HardGoal(
  "Strategic Blue Print for Website Be Followed",
  container = "CS Web Services"
)

n198 = N + SoftGoal(
  "Connect Back to the Community",
  container = "CS Web Services"
)

n199 = N + SoftGoal(
  "Maintain Services above Competition",
  container = "CS Web Services"
)

n200 = N + SoftGoal(
  "Encourage Kids Using Web Services to Use Phone Services",
  container = "CS Web Services"
)

n201 = N + SoftGoal(
  "Measure Success of Services",
  container = "CS Web Services"
)

n202 = N + SoftGoal(
  "Empowering Kids to Help Themselves",
  container = "CS Web Services"
)

n203 = N + SoftGoal(
  "Easier Navigation [CS Web Services]",
  container = "CS Web Services"
)

n204 = N + SoftGoal(
  "Avoid Presence of Pedofiles",
  container = "CS Web Services"
)

n205 = N + SoftGoal(
  "Reduce Contagion Effect[Of harmful Actions]",
  container = "CS Web Services"
)

n206 = N + SoftGoal(
  "Improve Image to Kids",
  container = "CS Web Services"
)

n208 = N + SoftGoal(
  "Immediacy",
  container = "CS Web Services"
)

n209 = N + SoftGoal(
  "Increase Emphasis on Online Feedback Form",
  container = "CS Web Services"
)

n210 = N + SoftGoal(
  "Similarity of Problems",
  container = "CS Web Services"
)

n211 = N + HardGoal(
  "Kids Use Online Information Provided",
  container = "CS Web Services"
)

n212 = N + SoftGoal(
  "Easier to Find Posts [Web Posting Technology]",
  container = "CS Web Services"
)

n213 = N + SoftGoal(
  "Effective chat room filters",
  container = "CS Web Services"
)

n214 = N + SoftGoal(
  "Avoid Dialogues [Between Kids]",
  container = "CS Web Services"
)

n215 = N + SoftGoal(
  "Avoid Bad Advice",
  container = "CS Web Services"
)

n216 = N + SoftGoal(
  "Avoid Dialogues Between[Kids and Counsellors on the Web]",
  container = "CS Web Services"
)

n217 = N + SoftGoal(
  "Control [Web Services]",
  container = "CS Web Services"
)

n218 = N + SoftGoal(
  "Sufficiently Moderated Web Services",
  container = "CS Web Services"
)

n219 = N + SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Web Services"
)

n220 = N + SoftGoal(
  "Decrease Response Time",
  container = "CS Web Services"
)

n221 = N + SoftGoal(
  "Direct Response to Kids",
  container = "CS Web Services"
)

n222 = N + SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Web Services"
)

n223 = N + Task(
  "Kids Read Polls about Kids",
  container = "CS Web Services"
)

n224 = N + Task(
  "Implement Polls about Kids",
  container = "CS Web Services"
)

n225 = N + Task(
  "Implement General Questions and Answers",
  container = "CS Web Services"
)

n226 = N + Task(
  "Implement Get Informed Section of Web Site",
  container = "CS Web Services"
)

n227 = N + Task(
  "Kids Read General Questions and Answers",
  container = "CS Web Services"
)

n228 = N + Task(
  "Kids Read Get Informed Section of Website",
  container = "CS Web Services"
)

n229 = N + Task(
  "Kids Get Information through E-Counselling",
  container = "CS Web Services"
)

n230 = N + SoftGoal(
  "Control of Counselling Work",
  container = "CS Web Services"
)

n231 = N + Task(
  "Put Content onto Website",
  container = "CS Web Services"
)

n232 = N + Task(
  "Acquire Web Content",
  container = "CS Web Services"
)

n233 = N + SoftGoal(
  "Reduce Number of Steps [Web Posting Technology]",
  container = "CS Web Services"
)

n234 = N + SoftGoal(
  "Correct Interpretation of Counsel",
  container = "CS Web Services"
)

n235 = N + HardGoal(
  "Technology that Does Not Allow Dialogue Between Kids Be Used",
  container = "CS Web Services"
)

n236 = N + HardGoal(
  "Technology that Allows Dialogue Between Kids Be Used",
  container = "CS Web Services"
)

n237 = N + HardGoal(
  "Anonymous Technology Be Used",
  container = "CS Web Services"
)

n238 = N + HardGoal(
  "Non-Anonymous Technology Be Used",
  container = "CS Web Services"
)

n239 = N + HardGoal(
  "Moderated E-Counselling Be Used",
  container = "CS Web Services"
)

n240 = N + HardGoal(
  "Non-Confidential Technology Be Used",
  container = "CS Web Services"
)

n241 = N + HardGoal(
  "Confidential Technology Be Used",
  container = "CS Web Services"
)

n242 = N + HardGoal(
  "Real Time E-Counselling Be Used",
  container = "CS Web Services"
)

n243 = N + HardGoal(
  "Non-Real Time E-Counselling Be Used",
  container = "CS Web Services"
)

n244 = N + SoftGoal(
  "Increased Web Services",
  container = "CS Web Services"
)

n245 = N + SoftGoal(
  "Anonymity [Counsellors]",
  container = "CS Web Services"
)

n246 = N + SoftGoal(
  "Friendly Web Site",
  container = "CS Web Services"
)

n247 = N + Task(
  "Kids Use Video Counselling",
  container = "CS Web Services"
)

n248 = N + Task(
  "Implement Video Counselling",
  container = "CS Web Services"
)

n249 = N + Task(
  "Kids Use Voice Counselling",
  container = "CS Web Services"
)

n250 = N + Task(
  "Implement Voice Counselling",
  container = "CS Web Services"
)

n251 = N + Task(
  "Kids Use Cyber Cafe/Portal/Chat Room",
  container = "CS Web Services"
)

n252 = N + Task(
  "Implement Cyber Cafe/Portal/Chat Room",
  container = "CS Web Services"
)

n253 = N + Task(
  "Implement Filters",
  container = "CS Web Services"
)

n254 = N + Task(
  "Block Kids who Display Inappropriate Behaviour",
  container = "CS Web Services"
)

n255 = N + Task(
  "Schedule Chat at Specific Times",
  container = "CS Web Services"
)

n256 = N + Task(
  "Implement Delay",
  container = "CS Web Services"
)

n257 = N + Task(
  "Kids Use Ask a Counsellor Section",
  container = "CS Web Services"
)

n258 = N + Task(
  "Maintain Ask a Counsellor Section",
  container = "CS Web Services"
)

n259 = N + Task(
  "Kids Use Text Messaging",
  container = "CS Web Services"
)

n260 = N + Task(
  "Implement Text Messaging",
  container = "CS Web Services"
)

n261 = N + SoftGoal(
  "Easier Access to Post Reply",
  container = "CS Web Services"
)

n262 = N + Task(
  "Inform Kids about Anonymity[Kids] of Web Services",
  container = "CS Web Services"
)

n263 = N + Task(
  "Kids Use One-On-One Chat Rooms",
  container = "CS Web Services"
)

n265 = N + Task(
  "Implement One-On-One Chat Rooms",
  container = "CS Web Services"
)

n267 = N + Task(
  "Kids Use Bulletin Board with Replies",
  container = "CS Web Services"
)

n268 = N + Task(
  "Implement Bulletin Board with Replies",
  container = "CS Web Services"
)

n269 = N + Task(
  "Kids Use Email Counselling",
  container = "CS Web Services"
)

n270 = N + Task(
  "Implement Email Counselling",
  container = "CS Web Services"
)

n271 = N + Task(
  "Kids Use Bulletin Board with Delayed Moderation",
  container = "CS Web Services"
)

n272 = N + Task(
  "Implement Bulletin Board with Delayed Moderation",
  container = "CS Web Services"
)

n273 = N + SoftGoal(
  "Kids Have Ownership of Services",
  container = "CS Phone Services"
)

n274 = N + Task(
  "Kids Use Phone Counselling",
  container = "CS Phone Services"
)

n275 = N + SoftGoal(
  "Connect Back to the Community",
  container = "CS Phone Services"
)

n276 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "CS Phone Services"
)

n277 = N + SoftGoal(
  "Confidentiality [Kids]",
  container = "CS Phone Services"
)

n278 = N + Task(
  "Maintain CS Phone Services",
  container = "CS Phone Services"
)

n279 = N + SoftGoal(
  "Determine Calls Coming from Web Users",
  container = "CS Phone Services"
)

n280 = N + Task(
  "Implement Anti-Pranking Message",
  container = "CS Phone Services"
)

n281 = N + SoftGoal(
  "Reduce Prank Calls",
  container = "CS Phone Services"
)

n282 = N + SoftGoal(
  "Decrease Phone Waiting Time",
  container = "CS Phone Services"
)

n283 = N + HardGoal(
  "Answer 80% of Calls within 30 Seconds of Message Ending",
  container = "CS Phone Services"
)

n284 = N + SoftGoal(
  "Connect Back to the Community",
  container = "PHL Phone Services"
)

n285 = N + SoftGoal(
  "Anonymity [Parents]",
  container = "PHL Phone Services"
)

n286 = N + Task(
  "Parents Use Phone Counselling",
  container = "PHL Phone Services"
)

n287 = N + Task(
  "Maintain PHL Phone Services",
  container = "PHL Phone Services"
)

n288 = N + Task(
  "Provide Recorded Messages",
  container = "PHL Phone Services"
)

n289 = N + SoftGoal(
  "Confidentiality [Parents]",
  container = "PHL Phone Services"
)

n290 = N + SoftGoal(
  "Anonymity [Parents]",
  container = "PHL Web Services"
)

n291 = N + SoftGoal(
  "Immediacy",
  container = "PHL Web Services"
)

n292 = N + SoftGoal(
  "Confidentiality [Parents]",
  container = "PHL Web Services"
)

n293 = N + SoftGoal(
  "Similarity with other parents' problems",
  container = "PHL Web Services"
)

n294 = N + SoftGoal(
  "Connect Back to the Community",
  container = "PHL Web Services"
)

n295 = N + Task(
  "Maintain PHL Web Services",
  container = "PHL Web Services"
)

n296 = N + SoftGoal(
  "Avoid Bad Advice",
  container = "PHL Web Services"
)

n297 = N + Task(
  "Parent Use Tool to Allow Parents to Talk to Each Other",
  container = "PHL Phone Services"
)

n298 = N + Task(
  "Implement Tool to Allow Parents to Talk to Each Other",
  container = "CS Phone Services"
)

n299 = N + Task(
  "Parent Use Bulletin Board with Replies",
  container = "PHL Phone Services"
)

n300 = N + Task(
  "Implement Board with Replies",
  container = "CS Phone Services"
)

n301 = N + Task(
  "Parent Use Information Section",
  container = "PHL Phone Services"
)

n302 = N + Task(
  "Implement Information Section",
  container = "CS Phone Services"
)

n303 = N + SoftGoal(
  "Easy [Access to Post Reply]",
  container = "CS Phone Services"
)

n304 = N + SoftGoal(
  "Friendly [Web Site]",
  container = "CS Phone Services"
)

n305 = N + Task(
  "Implement Tool to Allow Parents to Talk to Each Other",
  container = "Parents"
)

n306 = N + Task(
  "Parents Use Tool to Allow Parents to Talk to Each Other",
  container = "Parents"
)

n307 = N + Task(
  "Implement Board with Replies",
  container = "Parents"
)

n309 = N + Task(
  "Parents Use Bulletin Board with Replies",
  container = "Parents"
)

n310 = N + Task(
  "Implement Information Section",
  container = "Parents"
)

n311 = N + Task(
  "Parents Use Information Section",
  container = "Parents"
)

n312 = N + SoftGoal(
  "Friendly [Web Site]",
  container = "Parents"
)

n313 = N + Task(
  "Easy [Access to Post Reply]",
  container = "Parents"
)

n314 = N + Resource(
  "Phone Library of Recorded Messages",
  container = "Parents"
)

n315 = N + Task(
  "Kids use Video Counselling",
  container = "Kids and Youth"
)

n316 = N + Task(
  "Implement Video Counselling",
  container = "Kids and Youth"
)

n317 = N + Task(
  "Provide Web Counselling With Video",
  container = "Counselling"
)

n318 = N + Task(
  "Provide Web Counselling With Audio",
  container = "Counselling"
)

n319 = N + Task(
  "Kids Use Cyber Cafe/Portal/Chat Room",
  container = "Kids and Youth"
)

n320 = N + Task(
  "Implement Cyber Cafe/Portal/Chat Room",
  container = "Kids and Youth"
)

n321 = N + Task(
  "Kids Use Voice Counselling",
  container = "Kids and Youth"
)

n322 = N + Task(
  "Implement Voice Counselling",
  container = "Kids and Youth"
)

n323 = N + Task(
  "Moderate a Chat",
  container = "Kids and Youth"
)

n324 = N + SoftGoal(
  "Similarity of Problems",
  container = "Kids and Youth"
)

n325 = N + SoftGoal(
  "Connect to Other Kids",
  container = "Kids and Youth"
)

n326 = N + Task(
  "Kids use Text Messaging",
  container = "Kids and Youth"
)

n327 = N + Task(
  "Kids use Ask a Counsellor Section",
  container = "Kids and Youth"
)

n328 = N + Task(
  "Maintain Ask a Counsellor Section",
  container = "Kids and Youth"
)

n329 = N + Task(
  "Provide Written Counselling",
  container = "Counselling"
)

n330 = N + Task(
  "Easier Access to Post Reply",
  container = "Kids and Youth"
)

n331 = N + Task(
  "Inform Kids about Anonymity[Kids] of Web Services",
  container = "Kids and Youth"
)

n332 = N + Task(
  "Kids Use One-On-One Chat Rooms",
  container = "Kids and Youth"
)

n333 = N + Task(
  "Moderate Discussion Boards",
  container = "Kids and Youth"
)

n334 = N + Task(
  "Implement Text Messaging",
  container = "Kids and Youth"
)

n335 = N + Task(
  "Implement Bulletin Board With Replies",
  container = "Kids and Youth"
)

n336 = N + Task(
  "Implement One-On-ONe Chat Rooms",
  container = "Kids and Youth"
)

n337 = N + Task(
  "Create Counselling Posts",
  container = "Kids and Youth"
)

n338 = N + Task(
  "Kids Use Bulletin Board with Replies",
  container = "Kids and Youth"
)

n339 = N + Task(
  "Implement Email Counselling",
  container = "Kids and Youth"
)

n340 = N + Task(
  "Perform Email Counselling",
  container = "Kids and Youth"
)

n341 = N + Task(
  "Kids Use Email Counselling",
  container = "Kids and Youth"
)

n342 = N + Task(
  "Kids Use Bulletin Board with Delayed Moderation",
  container = "Kids and Youth"
)

n343 = N + Task(
  "Implement Bulletin Board with Delayed Moderation",
  container = "Kids and Youth"
)

n344 = N + SoftGoal(
  "Friendly Web Site",
  container = "Kids and Youth"
)

n345 = N + Task(
  "Kids Use Phone Counselling",
  container = "Kids and Youth"
)

n346 = N + SoftGoal(
  "Decrease Phone Waiting Time",
  container = "Kids and Youth"
)

n347 = N + Task(
  "Maintain Phone Services",
  container = "Kids and Youth"
)

n348 = N + Task(
  "Voice Counselling Be Performed",
  container = "Kids and Youth"
)

n349 = N + SoftGoal(
  "Anonymity [Kids]",
  container = "Kids and Youth"
)

n350 = N + SoftGoal(
  "Connect Back to the Community",
  container = "Kids and Youth"
)

n351 = N + SoftGoal(
  "Kids have Ownership of Services",
  container = "Kids and Youth"
)

n352 = N + SoftGoal(
  "Immediacy",
  container = "Kids and Youth"
)

n353 = N + SoftGoal(
  "Confidentiality [Kids]",
  container = "Kids and Youth"
)

n354 = N + SoftGoal(
  "Available [Services]",
  container = "Kids and Youth"
)

n355 = N + SoftGoal(
  "High Quality Services",
  container = "Kids and Youth"
)

n356 = N + Resource(
  "Feedback",
  container = "Kids and Youth"
)

#EDGES
E = Many()

e1 = E + Dep(
  source=n14,
  target=n2
)

e2 = E + Dep(
  source=n36,
  target=n3
)

e3 = E + Dep(
  source=n48,
  target=n4
)

e4 = E + Dep(
  source=n49,
  target=n5
)

e5 = E + Dep(
  source=n29,
  target=n6
)

e6 = E + Dep(
  source=n52,
  target=n7
)

e7 = E + Dep(
  source=n35,
  target=n8
)

e8 = E + Dep(
  source=n37,
  target=n9
)

e9 = E + Dep(
  source=n37,
  target=n9
)

e10 = E + Dep(
  source=n30,
  target=n10
)

e11 = E + Dep(
  source=n107,
  target=n12
)

e12 = E + Dep(
  source=n169,
  target=n12
)

e13 = E + Dep(
  source=n140,
  target=n13
)

e14 = E + Dep(
  source=n1,
  target=n15
)

e15 = E + Help(
  source=n20,
  target=n15
)

e16 = E + Help(
  source=n28,
  target=n15
)

e17 = E + Help(
  source=n17,
  target=n16
)

e18 = E + Help(
  source=n41,
  target=n16
)

e19 = E + Hurt(
  source=n33,
  target=n16
)

e20 = E + Dep(
  source=n116,
  target=n17
)

e21 = E + Dep(
  source=n60,
  target=n18
)

e22 = E + Dep(
  source=n118,
  target=n19
)

e23 = E + Dep(
  source=n88,
  target=n21
)

e24 = E + Dep(
  source=n121,
  target=n22
)

e25 = E + Dep(
  source=n122,
  target=n23
)

e26 = E + Dep(
  source=n125,
  target=n25
)

e27 = E + Dep(
  source=n126,
  target=n26
)

e28 = E + Dep(
  source=n145,
  target=n29
)

e29 = E + Or(
  source=n50,
  target=n29
)

e30 = E + Dep(
  source=n129,
  target=n30
)

e31 = E + Dep(
  source=n147,
  target=n31
)

e32 = E + Dep(
  source=n148,
  target=n32
)

e33 = E + Dep(
  source=n149,
  target=n33
)

e34 = E + Help(
  source=n102,
  target=n35
)

e35 = E + Help(
  source=n13,
  target=n36
)

e36 = E + Help(
  source=n16,
  target=n36
)

e37 = E + Help(
  source=n19,
  target=n36
)

e38 = E + Help(
  source=n21,
  target=n36
)

e39 = E + Help(
  source=n47,
  target=n36
)

e40 = E + Help(
  source=n23,
  target=n36
)

e41 = E + Help(
  source=n24,
  target=n36
)

e42 = E + Help(
  source=n25,
  target=n36
)

e43 = E + Help(
  source=n46,
  target=n36
)

e44 = E + Help(
  source=n32,
  target=n36
)

e45 = E + Help(
  source=n37,
  target=n36
)

e46 = E + Help(
  source=n34,
  target=n36
)

e47 = E + Help(
  source=n27,
  target=n37
)

e48 = E + Help(
  source=n40,
  target=n37
)

e49 = E + Help(
  source=n34,
  target=n37
)

e50 = E + Help(
  source=n19,
  target=n38
)

e51 = E + Help(
  source=n42,
  target=n38
)

e52 = E + Hurt(
  source=n33,
  target=n38
)

e53 = E + Help(
  source=n36,
  target=n39
)

e54 = E + Dep(
  source=n142,
  target=n40
)

e55 = E + Dep(
  source=n143,
  target=n41
)

e56 = E + Dep(
  source=n146,
  target=n42
)

e57 = E + Or(
  source=n48,
  target=n43
)

e58 = E + Or(
  source=n49,
  target=n43
)

e59 = E + Or(
  source=n29,
  target=n43
)

e60 = E + Or(
  source=n52,
  target=n43
)

e61 = E + Or(
  source=n49,
  target=n44
)

e62 = E + Or(
  source=n31,
  target=n45
)

e63 = E + Or(
  source=n51,
  target=n45
)

e65 = E + Dep(
  source=n128,
  target=n46
)

e66 = E + Dep(
  source=n80,
  target=n47
)

e67 = E + Dep(
  source=n351,
  target=n47
)

e68 = E + Or(
  source=n50,
  target=n48
)

e69 = E + Dep(
  source=n78,
  target=n48
)

e70 = E + Or(
  source=n50,
  target=n49
)

e71 = E + Dep(
  source=n123,
  target=n49
)

e72 = E + Dep(
  source=n11,
  target=n50
)

e73 = E + Dep(
  source=n124,
  target=n51
)

e74 = E + Or(
  source=n50,
  target=n52
)

e75 = E + Dep(
  source=n176,
  target=n52
)

e76 = E + Dep(
  source=n44,
  target=n53
)

e77 = E + Dep(
  source=n36,
  target=n54
)

e78 = E + Dep(
  source=n13,
  target=n55
)

e79 = E + Dep(
  source=n42,
  target=n56
)

e80 = E + Dep(
  source=n46,
  target=n57
)

e81 = E + Dep(
  source=n30,
  target=n58
)

e82 = E + Dep(
  source=n206,
  target=n59
)

e83 = E + Dep(
  source=n199,
  target=n60
)

e84 = E + Dep(
  source=n205,
  target=n62
)

e85 = E + Dep(
  source=n200,
  target=n63
)

e86 = E + Dep(
  source=n202,
  target=n65
)

e87 = E + Dep(
  source=n231,
  target=n71
)

e88 = E + Or(
  source=n75,
  target=n73
)

e89 = E + Or(
  source=n76,
  target=n73
)

e90 = E + Dep(
  source=n79,
  target=n74
)

e91 = E + Dep(
  source=n83,
  target=n75
)

e92 = E + Dep(
  source=n138,
  target=n76
)

e93 = E + Dep(
  source=n80,
  target=n77
)

e94 = E + Dep(
  source=n73,
  target=n78
)

e95 = E + Dep(
  source=n275,
  target=n79
)

e96 = E + Dep(
  source=n273,
  target=n80
)

e97 = E + Help(
  source=n223,
  target=n81
)

e98 = E + Help(
  source=n227,
  target=n81
)

e99 = E + Help(
  source=n228,
  target=n81
)

e100 = E + Dep(
  source=n81,
  target=n82
)

e101 = E + Dep(
  source=n195,
  target=n83
)

e102 = E + Dep(
  source=n195,
  target=n83
)

e103 = E + Dep(
  source=n203,
  target=n85
)

e104 = E + Dep(
  source=n220,
  target=n86
)

e105 = E + Dep(
  source=n201,
  target=n87
)

e106 = E + Dep(
  source=n218,
  target=n88
)

e107 = E + Or(
  source=n90,
  target=n89
)

e108 = E + Dep(
  source=n67,
  target=n90
)

e109 = E + Dep(
  source=n66,
  target=n91
)

e110 = E + Dep(
  source=n82,
  target=n92
)

e111 = E + Dep(
  source=n84,
  target=n93
)

e112 = E + Dep(
  source=n86,
  target=n95
)

e113 = E + Help(
  source=n114,
  target=n95
)

e114 = E + Dep(
  source=n134,
  target=n96
)

e115 = E + Help(
  source=n114,
  target=n96
)

e116 = E + Dep(
  source=n154,
  target=n97
)

e117 = E + Hurt(
  source=n109,
  target=n98
)

e118 = E + Help(
  source=n115,
  target=n99
)

e119 = E + Help(
  source=n108,
  target=n99
)

e120 = E + Help(
  source=n108,
  target=n99
)

e121 = E + Help(
  source=n112,
  target=n100
)

e122 = E + Help(
  source=n105,
  target=n100
)

e123 = E + Dep(
  source=n137,
  target=n101
)

e124 = E + Dep(
  source=n114,
  target=n103
)

e125 = E + Dep(
  source=n119,
  target=n105
)

e126 = E + Help(
  source=n94,
  target=n105
)

e127 = E + Dep(
  source=n133,
  target=n106
)

e128 = E + Dep(
  source=n87,
  target=n107
)

e129 = E + Help(
  source=n89,
  target=n107
)

e130 = E + Help(
  source=n92,
  target=n108
)

e131 = E + Make(
  source=n114,
  target=n108
)

e132 = E + Or(
  source=n111,
  target=n109
)

e133 = E + Or(
  source=n113,
  target=n109
)

e134 = E + Or(
  source=n97,
  target=n109
)

e135 = E + Dep(
  source=n83,
  target=n111
)

e136 = E + Dep(
  source=n83,
  target=n111
)

e137 = E + Dep(
  source=n68,
  target=n113
)

e138 = E + Dep(
  source=n132,
  target=n114
)

e139 = E + Dep(
  source=n85,
  target=n115
)

e140 = E + Dep(
  source=n106,
  target=n116
)

e141 = E + Dep(
  source=n77,
  target=n117
)

e142 = E + Dep(
  source=n104,
  target=n118
)

e143 = E + Dep(
  source=n20,
  target=n119
)

e144 = E + Dep(
  source=n103,
  target=n120
)

e145 = E + Dep(
  source=n102,
  target=n121
)

e146 = E + Dep(
  source=n101,
  target=n122
)

e147 = E + Dep(
  source=n109,
  target=n123
)

e148 = E + Dep(
  source=n89,
  target=n124
)

e149 = E + Dep(
  source=n100,
  target=n125
)

e150 = E + Dep(
  source=n99,
  target=n126
)

e151 = E + Dep(
  source=n27,
  target=n127
)

e152 = E + Dep(
  source=n74,
  target=n128
)

e153 = E + Dep(
  source=n98,
  target=n129
)

e154 = E + Dep(
  source=n196,
  target=n130
)

e155 = E + Dep(
  source=n244,
  target=n131
)

e156 = E + Dep(
  source=n276,
  target=n133
)

e157 = E + Dep(
  source=n194,
  target=n133
)

e158 = E + Dep(
  source=n217,
  target=n134
)

e159 = E + Dep(
  source=n221,
  target=n135
)

e160 = E + Dep(
  source=n219,
  target=n136
)

e161 = E + Dep(
  source=n215,
  target=n137
)

e162 = E + Dep(
  source=n296,
  target=n137
)

e163 = E + Dep(
  source=n278,
  target=n138
)

e164 = E + Dep(
  source=n291,
  target=n139
)

e165 = E + Dep(
  source=n160,
  target=n140
)

e166 = E + Dep(
  source=n28,
  target=n141
)

e167 = E + Dep(
  source=n171,
  target=n142
)

e168 = E + Dep(
  source=n165,
  target=n143
)

e169 = E + Dep(
  source=n172,
  target=n145
)

e170 = E + Dep(
  source=n170,
  target=n146
)

e171 = E + Dep(
  source=n168,
  target=n147
)

e172 = E + Dep(
  source=n41,
  target=n150
)

e173 = E + Dep(
  source=n290,
  target=n151
)

e174 = E + Dep(
  source=n289,
  target=n152
)

e175 = E + Dep(
  source=n292,
  target=n152
)

e176 = E + Dep(
  source=n284,
  target=n153
)

e177 = E + Dep(
  source=n294,
  target=n153
)

e178 = E + Dep(
  source=n295,
  target=n154
)

e179 = E + Dep(
  source=n287,
  target=n155
)

e180 = E + Dep(
  source=n286,
  target=n157
)

e181 = E + Dep(
  source=n293,
  target=n158
)

e182 = E + Dep(
  source=n167,
  target=n159
)

e183 = E + Help(
  source=n172,
  target=n160
)

e184 = E + Dep(
  source=n141,
  target=n161
)

e185 = E + Make(
  source=n172,
  target=n162
)

e186 = E + Dep(
  source=n132,
  target=n163
)

e187 = E + Dep(
  source=n138,
  target=n164
)

e188 = E + Break(
  source=n173,
  target=n165
)

e189 = E + Dep(
  source=n151,
  target=n165
)

e190 = E + Dep(
  source=n155,
  target=n166
)

e191 = E + Help(
  source=n163,
  target=n167
)

e192 = E + Help(
  source=n161,
  target=n167
)

e193 = E + Dep(
  source=n70,
  target=n168
)

e194 = E + Help(
  source=n168,
  target=n169
)

e195 = E + Hurt(
  source=n173,
  target=n170
)

e196 = E + Hurt(
  source=n167,
  target=n171
)

e197 = E + Or(
  source=n164,
  target=n172
)

e198 = E + Or(
  source=n166,
  target=n172
)

e199 = E + Dep(
  source=n69,
  target=n174
)

e200 = E + Dep(
  source=n153,
  target=n175
)

e201 = E + Or(
  source=n177,
  target=n176
)

e202 = E + Or(
  source=n178,
  target=n176
)

e203 = E + Dep(
  source=n154,
  target=n177
)

e204 = E + Dep(
  source=n155,
  target=n178
)

e205 = E + Dep(
  source=n223,
  target=n180
)

e206 = E + Dep(
  source=n225,
  target=n182
)

e207 = E + Dep(
  source=n226,
  target=n184
)

e208 = E + Dep(
  source=n209,
  target=n185
)

e209 = E + Dep(
  source=n212,
  target=n186
)

e210 = E + Dep(
  source=n245,
  target=n188
)

e211 = E + Dep(
  source=n214,
  target=n190
)

e212 = E + Dep(
  source=n233,
  target=n192
)

e213 = E + Dep(
  source=n230,
  target=n193
)

e214 = E + Dep(
  source=n133,
  target=n194
)

e215 = E + Make(
  source=n237,
  target=n194
)

e216 = E + Break(
  source=n238,
  target=n194
)

e217 = E + Hurt(
  source=n271,
  target=n194
)

e218 = E + Help(
  source=n221,
  target=n194
)

e219 = E + Or(
  source=n211,
  target=n195
)

e220 = E + Or(
  source=n239,
  target=n195
)

e221 = E + Dep(
  source=n72,
  target=n197
)

e222 = E + Help(
  source=n211,
  target=n198
)

e223 = E + Help(
  source=n239,
  target=n199
)

e224 = E + Help(
  source=n216,
  target=n200
)

e225 = E + Help(
  source=n209,
  target=n201
)

e226 = E + Help(
  source=n211,
  target=n202
)

e227 = E + Help(
  source=n261,
  target=n203
)

e228 = E + Dep(
  source=n61,
  target=n204
)

e229 = E + Break(
  source=n271,
  target=n204
)

e230 = E + Help(
  source=n217,
  target=n204
)

e231 = E + Help(
  source=n213,
  target=n205
)

e232 = E + Help(
  source=n214,
  target=n205
)

e233 = E + Help(
  source=n255,
  target=n205
)

e234 = E + Help(
  source=n256,
  target=n205
)

e235 = E + Hurt(
  source=n271,
  target=n205
)

e236 = E + Help(
  source=n199,
  target=n206
)

e237 = E + Help(
  source=n204,
  target=n206
)

e238 = E + Help(
  source=n211,
  target=n206
)

e239 = E + Help(
  source=n261,
  target=n206
)

e240 = E + Help(
  source=n219,
  target=n206
)

e241 = E + Help(
  source=n220,
  target=n206
)

e242 = E + Help(
  source=n220,
  target=n208
)

e243 = E + Make(
  source=n242,
  target=n208
)

e244 = E + Hurt(
  source=n243,
  target=n208
)

e245 = E + Help(
  source=n223,
  target=n210
)

e246 = E + Help(
  source=n227,
  target=n210
)

e247 = E + Help(
  source=n228,
  target=n210
)

e248 = E + Hurt(
  source=n235,
  target=n210
)

e249 = E + Help(
  source=n236,
  target=n210
)

e250 = E + Or(
  source=n223,
  target=n211
)

e251 = E + Or(
  source=n227,
  target=n211
)

e252 = E + Or(
  source=n228,
  target=n211
)

e253 = E + Or(
  source=n229,
  target=n211
)

e254 = E + Help(
  source=n251,
  target=n212
)

e255 = E + Help(
  source=n267,
  target=n212
)

e256 = E + Hurt(
  source=n271,
  target=n212
)

e257 = E + Make(
  source=n235,
  target=n214
)

e258 = E + Break(
  source=n236,
  target=n214
)

e259 = E + Help(
  source=n214,
  target=n215
)

e260 = E + Hurt(
  source=n242,
  target=n215
)

e261 = E + Help(
  source=n243,
  target=n215
)

e262 = E + Hurt(
  source=n247,
  target=n216
)

e263 = E + Hurt(
  source=n249,
  target=n216
)

e264 = E + Hurt(
  source=n251,
  target=n216
)

e265 = E + Help(
  source=n257,
  target=n216
)

e266 = E + Hurt(
  source=n259,
  target=n216
)

e267 = E + Hurt(
  source=n263,
  target=n216
)

e268 = E + Hurt(
  source=n267,
  target=n216
)

e269 = E + Hurt(
  source=n269,
  target=n216
)

e270 = E + Hurt(
  source=n271,
  target=n216
)

e271 = E + Help(
  source=n235,
  target=n217
)

e272 = E + Hurt(
  source=n235,
  target=n217
)

e273 = E + Hurt(
  source=n237,
  target=n217
)

e274 = E + Help(
  source=n238,
  target=n217
)

e275 = E + Hurt(
  source=n242,
  target=n217
)

e276 = E + Help(
  source=n243,
  target=n217
)

e277 = E + Hurt(
  source=n267,
  target=n218
)

e278 = E + Break(
  source=n240,
  target=n219
)

e279 = E + Make(
  source=n241,
  target=n219
)

e280 = E + Make(
  source=n242,
  target=n220
)

e281 = E + Hurt(
  source=n243,
  target=n220
)

e282 = E + Break(
  source=n257,
  target=n221
)

e283 = E + Help(
  source=n259,
  target=n221
)

e284 = E + Break(
  source=n267,
  target=n221
)

e285 = E + Make(
  source=n269,
  target=n221
)

e286 = E + Break(
  source=n271,
  target=n221
)

e287 = E + Help(
  source=n239,
  target=n222
)

e288 = E + Help(
  source=n262,
  target=n222
)

e289 = E + Dep(
  source=n181,
  target=n223
)

e290 = E + Or(
  source=n224,
  target=n223
)

e291 = E + Or(
  source=n231,
  target=n224
)

e292 = E + Or(
  source=n231,
  target=n225
)

e293 = E + Or(
  source=n231,
  target=n226
)

e294 = E + Dep(
  source=n179,
  target=n227
)

e295 = E + Or(
  source=n225,
  target=n227
)

e296 = E + Or(
  source=n226,
  target=n228
)

e297 = E + Dep(
  source=n183,
  target=n228
)

e298 = E + Or(
  source=n239,
  target=n229
)

e299 = E + Hurt(
  source=n239,
  target=n230
)

e300 = E + Dep(
  source=n71,
  target=n231
)

e301 = E + Or(
  source=n232,
  target=n231
)

e302 = E + Dep(
  source=n187,
  target=n232
)

e303 = E + Hurt(
  source=n258,
  target=n233
)

e304 = E + Hurt(
  source=n267,
  target=n233
)

e305 = E + Help(
  source=n271,
  target=n233
)

e306 = E + Help(
  source=n247,
  target=n234
)

e307 = E + Help(
  source=n249,
  target=n234
)

e308 = E + Hurt(
  source=n251,
  target=n234
)

e309 = E + Hurt(
  source=n257,
  target=n234
)

e310 = E + Hurt(
  source=n259,
  target=n234
)

e311 = E + Hurt(
  source=n263,
  target=n234
)

e312 = E + Hurt(
  source=n267,
  target=n234
)

e313 = E + Hurt(
  source=n269,
  target=n234
)

e314 = E + Hurt(
  source=n271,
  target=n234
)

e315 = E + Or(
  source=n247,
  target=n235
)

e316 = E + Or(
  source=n249,
  target=n235
)

e317 = E + Or(
  source=n257,
  target=n235
)

e318 = E + Or(
  source=n259,
  target=n235
)

e319 = E + Or(
  source=n263,
  target=n235
)

e320 = E + Or(
  source=n269,
  target=n235
)

e321 = E + Or(
  source=n251,
  target=n236
)

e322 = E + Or(
  source=n267,
  target=n236
)

e323 = E + Or(
  source=n271,
  target=n236
)

e324 = E + Or(
  source=n249,
  target=n237
)

e325 = E + Or(
  source=n257,
  target=n237
)

e326 = E + Or(
  source=n267,
  target=n237
)

e327 = E + Or(
  source=n247,
  target=n238
)

e328 = E + Or(
  source=n251,
  target=n238
)

e329 = E + Or(
  source=n259,
  target=n238
)

e330 = E + Or(
  source=n263,
  target=n238
)

e331 = E + Or(
  source=n269,
  target=n238
)

e332 = E + Or(
  source=n247,
  target=n239
)

e333 = E + Or(
  source=n249,
  target=n239
)

e334 = E + Or(
  source=n251,
  target=n239
)

e335 = E + Or(
  source=n257,
  target=n239
)

e336 = E + Or(
  source=n259,
  target=n239
)

e337 = E + Or(
  source=n263,
  target=n239
)

e338 = E + Or(
  source=n267,
  target=n239
)

e339 = E + Or(
  source=n269,
  target=n239
)

e340 = E + Or(
  source=n271,
  target=n239
)

e341 = E + Or(
  source=n251,
  target=n240
)

e342 = E + Or(
  source=n257,
  target=n240
)

e343 = E + Or(
  source=n267,
  target=n240
)

e344 = E + Or(
  source=n271,
  target=n240
)

e345 = E + Or(
  source=n247,
  target=n241
)

e346 = E + Or(
  source=n249,
  target=n241
)

e347 = E + Or(
  source=n259,
  target=n241
)

e348 = E + Or(
  source=n263,
  target=n241
)

e349 = E + Or(
  source=n269,
  target=n241
)

e350 = E + Or(
  source=n247,
  target=n242
)

e351 = E + Or(
  source=n249,
  target=n242
)

e352 = E + Or(
  source=n251,
  target=n242
)

e353 = E + Or(
  source=n259,
  target=n242
)

e354 = E + Or(
  source=n263,
  target=n242
)

e355 = E + Or(
  source=n257,
  target=n243
)

e356 = E + Or(
  source=n267,
  target=n243
)

e357 = E + Or(
  source=n269,
  target=n243
)

e358 = E + Or(
  source=n271,
  target=n243
)

e359 = E + Help(
  source=n247,
  target=n244
)

e360 = E + Help(
  source=n249,
  target=n244
)

e361 = E + Help(
  source=n251,
  target=n244
)

e362 = E + Help(
  source=n257,
  target=n244
)

e363 = E + Help(
  source=n259,
  target=n244
)

e364 = E + Help(
  source=n263,
  target=n244
)

e365 = E + Help(
  source=n267,
  target=n244
)

e366 = E + Help(
  source=n269,
  target=n244
)

e367 = E + Help(
  source=n271,
  target=n244
)

e368 = E + Hurt(
  source=n247,
  target=n245
)

e369 = E + Hurt(
  source=n249,
  target=n245
)

e370 = E + Help(
  source=n251,
  target=n245
)

e371 = E + Help(
  source=n257,
  target=n245
)

e372 = E + Help(
  source=n259,
  target=n245
)

e373 = E + Help(
  source=n263,
  target=n245
)

e374 = E + Help(
  source=n267,
  target=n245
)

e375 = E + Hurt(
  source=n269,
  target=n245
)

e376 = E + Help(
  source=n271,
  target=n245
)

e377 = E + Hurt(
  source=n221,
  target=n245
)

e378 = E + Help(
  source=n244,
  target=n246
)

e379 = E + Help(
  source=n221,
  target=n246
)

e380 = E + Help(
  source=n208,
  target=n246
)

e381 = E + Help(
  source=n203,
  target=n246
)

e382 = E + Or(
  source=n248,
  target=n247
)

e383 = E + Dep(
  source=n317,
  target=n248
)

e384 = E + Or(
  source=n250,
  target=n249
)

e385 = E + Dep(
  source=n318,
  target=n250
)

e386 = E + Dep(
  source=n322,
  target=n250
)

e387 = E + Or(
  source=n252,
  target=n251
)

e388 = E + Dep(
  source=n319,
  target=n251
)

e389 = E + Or(
  source=n253,
  target=n252
)

e390 = E + Or(
  source=n254,
  target=n252
)

e391 = E + Or(
  source=n255,
  target=n252
)

e392 = E + Or(
  source=n256,
  target=n252
)

e393 = E + Or(
  source=n258,
  target=n257
)

e394 = E + Dep(
  source=n327,
  target=n257
)

e395 = E + Dep(
  source=n328,
  target=n258
)

e396 = E + Dep(
  source=n333,
  target=n258
)

e397 = E + Dep(
  source=n337,
  target=n258
)

e398 = E + Or(
  source=n260,
  target=n259
)

e399 = E + Dep(
  source=n334,
  target=n260
)

e400 = E + Dep(
  source=n329,
  target=n260
)

e401 = E + Help(
  source=n257,
  target=n261
)

e402 = E + Or(
  source=n265,
  target=n263
)

e403 = E + Dep(
  source=n336,
  target=n265
)

e404 = E + Dep(
  source=n329,
  target=n265
)

e405 = E + Or(
  source=n268,
  target=n267
)

e406 = E + Dep(
  source=n338,
  target=n267
)

e407 = E + Dep(
  source=n333,
  target=n268
)

e408 = E + Dep(
  source=n337,
  target=n268
)

e409 = E + Or(
  source=n270,
  target=n269
)

e410 = E + Dep(
  source=n341,
  target=n269
)

e411 = E + Dep(
  source=n339,
  target=n270
)

e412 = E + Dep(
  source=n340,
  target=n270
)

e413 = E + Or(
  source=n272,
  target=n271
)

e414 = E + Dep(
  source=n342,
  target=n271
)

e415 = E + Dep(
  source=n333,
  target=n272
)

e416 = E + Dep(
  source=n337,
  target=n272
)

e417 = E + Dep(
  source=n343,
  target=n272
)

e418 = E + Make(
  source=n274,
  target=n273
)

e419 = E + Or(
  source=n278,
  target=n274
)

e420 = E + Help(
  source=n274,
  target=n275
)

e421 = E + Make(
  source=n274,
  target=n276
)

e422 = E + Help(
  source=n274,
  target=n277
)

e423 = E + Or(
  source=n283,
  target=n278
)

e424 = E + Dep(
  source=n348,
  target=n278
)

e425 = E + Dep(
  source=n189,
  target=n281
)

e426 = E + Help(
  source=n280,
  target=n281
)

e427 = E + Hurt(
  source=n277,
  target=n281
)

e428 = E + Help(
  source=n283,
  target=n282
)

e429 = E + Help(
  source=n286,
  target=n284
)

e430 = E + Make(
  source=n286,
  target=n285
)

e431 = E + Or(
  source=n287,
  target=n286
)

e432 = E + Or(
  source=n288,
  target=n287
)

e433 = E + Help(
  source=n286,
  target=n289
)

e434 = E + Help(
  source=n299,
  target=n290
)

e435 = E + Help(
  source=n297,
  target=n291
)

e436 = E + Hurt(
  source=n299,
  target=n291
)

e437 = E + Break(
  source=n299,
  target=n292
)

e438 = E + Help(
  source=n297,
  target=n293
)

e439 = E + Help(
  source=n299,
  target=n293
)

e440 = E + Help(
  source=n297,
  target=n294
)

e441 = E + Help(
  source=n299,
  target=n294
)

e442 = E + Help(
  source=n301,
  target=n294
)

e443 = E + Or(
  source=n298,
  target=n295
)

e444 = E + Or(
  source=n300,
  target=n295
)

e445 = E + Or(
  source=n302,
  target=n295
)

e446 = E + Hurt(
  source=n297,
  target=n296
)

e447 = E + Or(
  source=n298,
  target=n297
)

e448 = E + Dep(
  source=n306,
  target=n297
)

e449 = E + Or(
  source=n300,
  target=n299
)

e450 = E + Dep(
  source=n309,
  target=n299
)

e451 = E + Or(
  source=n302,
  target=n301
)

e452 = E + Dep(
  source=n311,
  target=n301
)

e453 = E + Hurt(
  source=n299,
  target=n303
)

e454 = E + Dep(
  source=n291,
  target=n304
)

e455 = E + Dep(
  source=n298,
  target=n305
)

e456 = E + Dep(
  source=n300,
  target=n307
)

e457 = E + Dep(
  source=n302,
  target=n310
)

e458 = E + Dep(
  source=n304,
  target=n312
)

e459 = E + Dep(
  source=n303,
  target=n313
)

e460 = E + Dep(
  source=n288,
  target=n314
)

e461 = E + Dep(
  source=n248,
  target=n316
)

e462 = E + Dep(
  source=n323,
  target=n252
)

e463 = E + Dep(
  source=n210,
  target=n324
)

e464 = E + Dep(
  source=n236,
  target=n325
)

e465 = E + Dep(
  source=n259,
  target=n326
)

e466 = E + Dep(
  source=n329,
  target=n252
)

e467 = E + Dep(
  source=n261,
  target=n330
)

e468 = E + Dep(
  source=n262,
  target=n331
)

e469 = E + Dep(
  source=n263,
  target=n332
)

e470 = E + Dep(
  source=n335,
  target=n268
)

e471 = E + Dep(
  source=n246,
  target=n344
)

e472 = E + Dep(
  source=n345,
  target=n274
)

e473 = E + Dep(
  source=n282,
  target=n346
)

e474 = E + Dep(
  source=n278,
  target=n347
)

e475 = E + Dep(
  source=n348,
  target=n287
)

e476 = E + Dep(
  source=n17,
  target=n349
)

e477 = E + Dep(
  source=n46,
  target=n350
)

e478 = E + Dep(
  source=n47,
  target=n351
)

e479 = E + Dep(
  source=n13,
  target=n352
)

e480 = E + Dep(
  source=n19,
  target=n353
)

e481 = E + Dep(
  source=n30,
  target=n354
)

e482 = E + Dep(
  source=n36,
  target=n355
)

e483 = E + Or(
  source=n45,
  target=n33
)

e484 = E + Or(
  source=n33,
  target=n356
)


graph = Graph("CSServices", N.all, E.all)