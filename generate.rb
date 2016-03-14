require 'axlsx'
require 'pg'

# Housing Charts
class Munger
  # Takes a sheet, a batch, and sql, and lays out data on a grid,
  # with some options
  def initialize(sheet, batch, sql, headings)
    @sheet = sheet
    @batch = batch
    @sql = sql
    @headings = headings
  end

  def data
    @batch.connection.exec_params(@sql)
  end

  def values
    data.values
  end

  def fields
    data.fields
  end

  def munge
    yield(data)
  end

  def generate
    @sheet.add_row #here we progressively add the rows
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

  def initialize(workbook, muni_id)
    @workbook = workbook
    @muni_id = muni_id
  end

  def connection
    PG::Connection.open(dbname: 'ds', host: '10.10.10.240', user:'dsviewer', password:'dsview933')
  end
end

class Chart
  attr_reader :batch

  def initialize(batch, title)
    @batch = batch
    @title = title
  end

  def workbook
    @batch.workbook.workbook
  end

  def data
    "Test"
  end

  def column
  end

  def generate
    workbook.add_worksheet(name: @title) do |sheet|
      yield(sheet, data)
    end
  end
end

workbook = Workbook.new
batch = Batch.new(workbook)
# chart = Chart.new(batch, "CostBurdenSubregion")
