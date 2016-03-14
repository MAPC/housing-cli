require 'axlsx'
require 'pg'

# Housing Charts
class Munger
  def initialize(args)

  end
end

class Workbook
  attr_reader :excel

  def initialize 
    @excel = Axlsx::Package.new
  end

  def workbook
    @excel.workbook
  end

  def some_other_stuff

  end
end

class Batch
  attr_reader :workbook

  def initialize(workbook)
    @workbook = workbook
  end

  def connection
    PG::Connection.open(dbname: 'ds', host: '******', user:'******', password:'******')
  end
end

class Chart
  attr_reader :batch

  def initialize(batch)
    @batch = batch
  end

  def generate
    @batch.workbook.workbook.add_worksheet(name: "TestAsdf") do |sheet|

    end
  end
end

workbook = Workbook.new
batch = Batch.new(workbook)
chart = Chart.new(batch)
