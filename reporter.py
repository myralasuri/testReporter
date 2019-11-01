from django.shortcuts import render

# Create your views here.
def getb():
   banner = """
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
   <a class="navbar-brand" href="#">Innominds</a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
   </button>

   <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
      </ul>
      <form class="form-inline my-2 my-lg-0">
         <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
         <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
   </div>
   </nav>
      """
   return banner

def welcome(request):
   names=['suit1','suit2','suit3','suit4']
   snos=[1,2,3,4]
   statuses=['passed','passed','passed','passed']
   times=['1.24','2.43546','3.454','2.3456']
   cons=[names,snos,statuses,times]

   banner = getb()
   rows =''
   cons=[names,snos,statuses,times]
   s = [[arr[i] for arr in cons] for i in range(len(names)) ]
   dicts=[]
   for i in s:
      dicts.append(dict(zip(['name','sno','status','time'], i)))
   print(dicts)
   for suit in dicts:
      it = suit
      createModule(suit=it['name'], module= {'name': 'module1', 'executed':8, 'passed':9, 'failed':8, 'skipped': 0, 'percentage': 23, 'duartion':789})
      rows += """
               <tr>
            <td >{sno}</td>
            <td ><a href='./{name}.html'>{name}</td>
            <td >{status}</td>
            <td >{time}</td>
         </tr>
      """.format(sno = it['sno'], name=it['name'], time='0.678', status=it['status'])

   re = """ <html>
   <head></head>
   <body>
   {banner}
   <div class="mx-auto" style="width: 200px;">
   </div>
   <div class ='container mx-auto' style='margin-top:50px'>
      <table class="table">
          <thead class="thead-dark">
         <tr>
            <th>S.no</th>
            <th>SuitName</th>
            <th>Status</th>
            <th>TimeTaken</th>
         </tr>
         </thead>
         {rows}
      </table>
      </div>  """.format(banner=banner,rows=rows)
      
   file1 = open('suit.html','w')
   file1.write(re)
   file1.close()

    #   open()
   return render(request, 'reporter.html', {'da':re})   
def createModule(suit,module):
   module = [{'name': 'module1', 'executed':2, 'passed':3, 'failed':7, 'skipped':0},
   {'name': 'module2', 'executed':2, 'passed':3, 'failed':7, 'skipped':0},
   {'name': 'module3', 'executed':2, 'passed':3, 'failed':7, 'skipped':0},
   {'name': 'module4', 'executed':2, 'passed':3, 'failed':7, 'skipped':0}]
   rows=''
   for tc in module:
      it = tc
      tsc=''
      testcase  = [{'name':'sdfgh','ts': 'testcase1','status':'failed'},
      {'name':'sdfgh','ts': 'testcase1','status':'failed'},
      {'name':'sdfgh','ts': 'testcase1','status':'failed'},
      {'name':'sdfgh','ts': 'testcase1','status':'failed'}]
      for step in testcase:
         tsc += """ <tr>
            <td >{module}</td>
            <td >{ts}</td>
            <td >{status}</td>
         </tr>
      """.format(module=step['name'], ts=step['ts'],status=step['status'])
      cont = """
                  <html>
               <head></head>
               <body>
               {banner}
                  <div class="mx-auto" style="width: 200px;">
                  </div>
                  <div class ='container mx-auto' style='margin-top:50px'>
                  <table class="table">
                     <thead class='thead-dark'>
                     <tr>
                        <th>Name of the Module</th>
                        <th >Test case Name</th>
                        <th >Status</th>
                     </tr>
                     </thead>
                     <tbody>
                     {tsc}
                     </tbody>
                  </table>
               </body>
            </html>
      """.format(tsc=tsc, banner=getb())
      print("at create module files")
      file1 = open('./'+tc['name']+ '.html','w')
      file1.write(cont)
      file1.close()
      rows += """ <tr>
            <td ><a href='./{name}.html'>{name}</td>
            <td >{executed}</td>
            <td >{passed}</td>
            <td >{failed}</td>
            <td >{skipped}</td>
            <td >00.00%</td>
            <td >15 Second(s).</td>
         </tr>
      """.format(name=tc['name'], executed=it['executed'],passed=it['passed'], failed=it['failed'], skipped=it['skipped'])
   con = """ <html>
   <head></head>
   <body>
   {banner}
   <div class="mx-auto" style="width: 200px;">
   </div>
   <div class ='container mx-auto' style='margin-top:50px'></div>
      <div class='card-header'>status of  {suit}</div>
      <table  class="table">
         <thead class="thead-dark">
         <tr>
            <th>Name of the module</th>
            <th>Executed</th>
            <th>Passed</th>
            <th>Failed</th>
            <th>Skipped</th>
            <th>Pass Percentage</th>
            <th>Time Taken for Execution</th>
         </tr>
         </thead>
         {rows}
      </table>
      </div>""".format(banner=getb(),rows=rows, suit='suit')
   
   file1 = open('./'+str(suit)+ '.html','w')
   file1.write(con)
   file1.close()
   
   # print("at create module files")

def show(request, fielname=None, modules='modules'):
   banner = getb()
   rows =''
   suits = [{'name': 'm1', 'executed':10, 'failed':3, 'passed': 7, 'skipped':0},
   {'name': 'm2', 'executed':10, 'failed':3, 'passed': 7, 'skipped':0},
   {'name': 'm3', 'executed':10, 'failed':3, 'passed': 7, 'skipped':0},
   {'name': 'm4', 'executed':10, 'failed':3, 'passed': 7, 'skipped':0}]
   for itm in suits:
      createModule({'name': 'module2', 'executed':8, 'passed':9, 'failed':8, 'skipped': 0, 'percentage': 23, 'duartion':789})
      it = itm
      rows += """
               <tr>
            <td style = "background: #E0EEEE; color: #000; font-weight: bold;text-align: left;width:15%"><a href='./{name}.html'>{name}</td>
            <td >{executed}</td>
            <td >{passed}</td>
            <td >{failed}</td>
            <td >{skipped}</td>
            <td >00.00%</td>
            <td >15 Second(s).</td>
         </tr>
      """.format(name=it['name'], executed=it['executed'],passed=it['passed'], failed=it['failed'], skipped=it['skipped'])

   re = """ <html>
   <head></head>
   <body>
   {banner}
      <table>
         <th>
         <tr>
            <td  >Name of the Module</td>
            <td  >Executed</td>
            <td  >Passed</td>
            <td  >Failed</td>
            <td  >Skipped</td>
            <td  >Pass Percentage</td>
            <td  >Time Taken for Execution</td>
         </tr>
         </th>
         {rows}
      </table>  """.format(banner=banner,rows=rows)
   file1 = open('suit.html','w')
   file1.write(re)
   file1.close()

    #   open()
   return render(request, 'reporter.html', {'da':re})
